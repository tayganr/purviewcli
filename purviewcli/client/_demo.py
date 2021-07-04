import math, time, json, string, random, importlib.resources, tempfile, os
from datetime import datetime
from subprocess import Popen, PIPE

def runCommand(cmd):
    # print('calling')
    output = Popen(cmd.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0].decode('ascii')
    output = json.loads(output)
    return output

def provisionResourceGroup(subscriptionId, location, resourceGroupName):
    resourceGroupName = resourceGroupName or 'purview-rg-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    cmd = f"pv management putResourceGroup --subscriptionId {subscriptionId} --resourceGroupName {resourceGroupName} --location {location}"
    data = runCommand(cmd)
    print(f'Resource Group: {resourceGroupName}')
    return resourceGroupName

def provisionAccount(subscriptionId, location, resourceGroupName):
    # Generate unique name
    accountName = None
    nameAvailable = False
    while nameAvailable == False:
        accountName = 'purview-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        cmd = f"pv management checkNameAvailability --subscriptionId {subscriptionId} --accountName {accountName}"
        data = runCommand(cmd)
        nameAvailable = data['nameAvailable']
    print(f'Account Name: {accountName}')

    # Provision Azure Purview Account
    payload = {
        "identity": {
            "type": "SystemAssigned"
        },
        "location": location,
        "sku": {
            "name": "Standard",
            "capacity": 4
        }
    }
    fd, path = tempfile.mkstemp(suffix='.json')
    try:
        with os.fdopen(fd, 'w') as tmp:
            json.dump(payload, tmp)
        print('Provisioning Azure Purview account...')
        cmd = f"pv management createAccount --subscriptionId {subscriptionId} --resourceGroupName {resourceGroupName} --accountName {accountName} --payload-file {path}"
        data = runCommand(cmd)
    finally:
        os.remove(path)

    # Check provisioningState until Succeeded
    provisioning = True
    while provisioning:
        time.sleep(30)
        cmd = f"pv management readAccount --subscriptionId {subscriptionId} --resourceGroupName {resourceGroupName} --accountName {accountName}"
        data = runCommand(cmd)
        if data['properties']['provisioningState'] == 'Succeeded':
            provisioning = False

    print(f'Ready! Purview Studio: https://ms.web.purview.azure.com/resource/{accountName}')
    return accountName

def assignRole(subscriptionId, resourceGroupName, accountName, roleDefinitionId):
    cmd = "pv graph readMe"
    data = runCommand(cmd)
    principalId = data['id']
    userPrincipalName = data['userPrincipalName']
    print(f'Assigning role [User Access Administrator] to [principalId: {principalId}; userPrincipalName: {userPrincipalName}]')
    cmd = f"pv management putRoleAssignment --subscriptionId {subscriptionId} --resourceGroupName {resourceGroupName} --accountName {accountName} --roleDefinitionId {roleDefinitionId} --principalId {principalId}"
    data = runCommand(cmd)

def populateTypes(accountName):
    print(' - Creating custom type definitions...')
    with importlib.resources.path("purviewcli.ninja", "typedefs_custom.json") as filepath:
        cmd = f"pv types createTypeDefs --payload-file {filepath} --purviewName {accountName}"
        data = runCommand(cmd)

def populateEntities(accountName):
    # 1. Read entities.json
    # 
    # 2. Generate entities_min_rels.json
    #    Include: guid, attributes, relationshipAttributes, contacts, status, typeName, classifications.classification.typeName
    # 
    # 3. Generate entities_min_worels.json
    #    Drop: guid, attributes.inputs, attributes.outputs, relationshipAttributes
    # 
    # 4. Split entities_min_worels.json (primary/secondary)
    # 
    # 5. Generate entities_min_rels_new with new GUIDs

    # 1. Read entities.json
    with importlib.resources.path("purviewcli.ninja", "entities.json") as filepath:
        with open(filepath) as f:
            entities = json.load(f)

    # 2. Generate entities_min_rels.json
    entities_min_rels = []
    item = {}
    for entity in entities:
        item = {
            'guid': entity['guid'],
            'attributes': entity['attributes'],
            'relationshipAttributes': entity['relationshipAttributes'],
            'status': entity['status'],
            'typeName': entity['typeName'],
        }
        if 'contacts' in entity:
            item['contacts'] = entity['contacts']
        if 'classifications' in entity:
            item['classifications'] = []
            for classification in entity['classifications']:
                item['classifications'].append({ 'typeName': classification['typeName'] })
        entities_min_rels.append(item)

    # 3. Generate entities_min_worels.json
    #    Drop: guid, attributes.inputs, attributes.outputs, relationshipAttributes
    entities_min_worels = []
    item = {}
    for entity in entities_min_rels:
        item = {
            'attributes': entity['attributes'],
            'status': entity['status'],
            'typeName': entity['typeName'],
        }
        item['attributes'].pop('inputs', None)
        item['attributes'].pop('outputs', None)
        entities_min_worels.append(item)

    # 4. Split entities_min_worels.json (primary/secondary)
    entities_primary = { "entities": [] }
    entities_secondary = { "entities": [] }
    for entity in entities_min_worels:
        typeName = entity['typeName'].upper()
        if 'COLUMN' in typeName or typeName.startswith('JSON_PROPERTY') or typeName.startswith('JSON_SCHEMA'):
            entities_secondary['entities'].append(entity)
        else:
            entities_primary['entities'].append(entity)

    # 5. MAP: qualifiedName to OLD GUID
    old_entities = {}
    for entity in entities:
        qualifiedName = entity['attributes']['qualifiedName']
        old_guid = entity['guid']
        old_entities[qualifiedName] = old_guid

    # 6. Bulk Create Entities (without relationships)
    guid_mapping = {}
    collections = [entities_primary, entities_secondary]
    for collection in collections:
        fd, path = tempfile.mkstemp(suffix='.json')
        with os.fdopen(fd, 'w') as tmp:
            json.dump(collection, tmp)
        print(f' - Creating entities from {path}...')
        cmd = f"pv entity createBulk --payload-file {path} --purviewName {accountName}"
        guidAssignments = runCommand(cmd)
        os.remove(path)
        counter = 0
        for entity in collection['entities']:
            new_guid = list(guidAssignments['guidAssignments'].items())[counter][1]
            qualifiedName = entity['attributes']['qualifiedName']
            old_guid = old_entities[qualifiedName]
            guid_mapping[old_guid] = new_guid
            counter += 1

    # 7. Generate entities_min_rels_new.json (with new GUIDs)
    entities_min_rels_new = { "entities": [] }
    for entity in entities_min_rels:
        # Inputs/Outputs
        for attribute in entity['attributes']:
            if attribute == 'inputs' or attribute == 'outputs':
                for io in entity['attributes'][attribute]:
                    if 'guid' in io:
                        old_guid = io['guid']
                        io['guid'] = guid_mapping[old_guid]
        # Relationships
        for relationshipAttribute in entity['relationshipAttributes']:
            attr = entity['relationshipAttributes'][relationshipAttribute]
            isList = True if type(attr) is list else False
            if isList:
                for element in attr:
                    old_guid = element['guid']
                    element['guid'] = guid_mapping[old_guid]
                    element.pop('relationshipGuid', None)
            else:
                old_guid = attr['guid']
                attr['guid'] = guid_mapping[old_guid]
                attr.pop('relationshipGuid', None)
        # Pop GUID
        entity.pop('guid', None)
        entities_min_rels_new['entities'].append(entity)

    # 8. Bulk Create Entities (with relationships)
    fd, path = tempfile.mkstemp(suffix='withrels.json')
    print(f' - Creating entities with relationships from {path}...')
    with os.fdopen(fd, 'w') as tmp:
        json.dump(entities_min_rels_new, tmp)
    cmd = f"pv entity createBulk --payload-file {path} --purviewName {accountName}"
    data = runCommand(cmd)
    # os.remove(path)

def populateSources(accountName):
    with importlib.resources.path("purviewcli.ninja", "sources.json") as filepath:
        print(f' - Creating sources from {filepath}...')
        with open(filepath) as f:
            sources = json.load(f)

    for source in sources:
        dataSourceName = source['name']
        fd, path = tempfile.mkstemp(suffix='.json')
        try:
            with os.fdopen(fd, 'w') as tmp:
                json.dump(source, tmp, indent=4, sort_keys=True)
            cmd = f"pv scan putDataSource --dataSourceName {dataSourceName} --payload-file {path} --purviewName {accountName}"
            data = runCommand(cmd)
        finally:
            os.remove(path)

class Demo():
    def demoGenerate(self, args):
        # Init variables
        resourceGroupName = args['--resourceGroupName']
        subscriptionId = args['--subscriptionId']
        location = args['--location']

        # Start Timestamp
        startTime = datetime.now()

        # Provision Resources
        resourceGroupName = provisionResourceGroup(subscriptionId, location, resourceGroupName)
        accountName = provisionAccount(subscriptionId, location, resourceGroupName)

        # Add Role Assignment (Owner)
        roleDefinitionId = '18d7d88d-d35e-4fb5-a5c3-7773c20a72d9' # User Access Administrator
        assignRole(subscriptionId, resourceGroupName, accountName, roleDefinitionId)
        
        # Populate account
        print('Populating environment...')
        populateTypes(accountName)
        populateEntities(accountName)
        populateSources(accountName)
        
        # Complete
        print('Complete!')

        # Calculate Total Duration
        finishTime = datetime.now()
        duration = finishTime - startTime
        minutes = math.floor(duration.seconds / 60)
        seconds = duration.seconds % 60
        print(f'Duration: {minutes:02}:{seconds:02}')
        
        response = ' '
        return response
