import math, time, json, string, random, importlib.resources, random, sys, requests, uuid
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ClientAuthenticationError

def get_token(app):
    credential = DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True,
        exclude_shared_token_cache_credential=True
    )

    if app == "management":
        resource = "https://management.azure.com/.default"
    elif app == 'graph':
        resource = "https://graph.microsoft.com/.default"
    else:
        resource = "https://purview.azure.net/.default"

    try:
        token = credential.get_token(f'{resource}')
    except ClientAuthenticationError as e:
        print(e)
        print("For more information, check out: https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python")
        sys.exit()
    return token.token

def http_get(method, endpoint, params, payload, access_token):
    headers = {"Authorization": "Bearer {0}".format(access_token)}

    try:
        response = requests.request(method, endpoint, params=params, json=payload, headers=headers)
    except requests.exceptions.HTTPError as errh:
        print ("[HTTP ERROR]",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("[CONNECTION ERROR]",errc)
        sys.exit()
    except requests.exceptions.Timeout as errt:
        print ("[TIMEOUT ERROR]",errt)
    except requests.exceptions.RequestException as err:
        print ("[REQUEST EXCEPTION]",err)

    status_code = response.status_code
    if status_code == 204:
        data = {
            'operation': '[%s] %s' % (method, response.url),
            'status': 'The server successfully processed the request'
        }
    else:
        try:
            data = response.json()
        except ValueError:
            data = {
                'url': response.url,
                'status_code': response.status_code,
                'reason': response.reason
            }
    return data

class Demo():

    def __init__(self):
        self.token_purview = get_token('purview')
        self.token_management = get_token('management')
        self.token_graph = get_token('graph')

    def provisionResourceGroup(self, subscriptionId, location, resourceGroupName):
        resourceGroupName = resourceGroupName or 'purview-rg-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = { 'api-version': '2021-04-01' }
        payload = { 'location': location }
        data = http_get(method, endpoint, params, payload, self.token_management)
        print(f'Resource Group: {resourceGroupName}')
        return resourceGroupName

    def provisionStorageAccount(self, subscriptionId, location, resourceGroupName):
        accountName = 'adls' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'
        params = { 'api-version': '2018-02-01' }
        payload = {
            "sku": {
                "name": "Standard_LRS"
            },
            "properties": {
                "isHnsEnabled": True
            },
            "kind": "StorageV2",
            "location": location,
        }
        data = http_get(method, endpoint, params, payload, self.token_management)
        print(f'ADLS Gen2 Storage Account: {accountName}')
        return accountName

    def provisionAccount(self, subscriptionId, location, resourceGroupName):
        # Generate unique name
        accountName = None
        nameAvailable = False
        while nameAvailable == False:
            accountName = 'purview-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            method = 'POST'
            endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Purview/checkNameAvailability'
            params = {'api-version': '2020-12-01-preview'}
            payload = {'name': accountName, 'type': 'Microsoft.Purview/accounts'}
            data = http_get(method, endpoint, params, payload, self.token_management)
            nameAvailable = data['nameAvailable']
        print(f'Account Name: {accountName}')

        # Provision Azure Purview Account
        print('Provisioning Azure Purview account...')
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        params = {'api-version': '2020-12-01-preview'}
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
        data = http_get(method, endpoint, params, payload, self.token_management)

        # Check provisioningState until Succeeded
        time.sleep(60)
        provisioning = True
        while provisioning:
            time.sleep(5)
            method = 'GET'
            endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
            params = {'api-version': '2020-12-01-preview'}
            payload = None
            data = http_get(method, endpoint, params, payload, self.token_management)
            if data['properties']['provisioningState'] == 'Succeeded':
                provisioning = False

        print(f'Ready! Purview Studio: https://ms.web.purview.azure.com/resource/{accountName}')
        return accountName

    def assignRole(self, subscriptionId, resourceGroupName, accountName, roleDefinitionId):
        method = 'GET'
        endpoint = 'https://graph.microsoft.com/v1.0/me'
        params = None
        payload = None
        data = http_get(method, endpoint, params, payload, self.token_graph)
        principalId = data['id']
        userPrincipalName = data['userPrincipalName']
        print(f'Assigning role [User Access Administrator] to [principalId: {principalId}; userPrincipalName: {userPrincipalName}]')
        method = 'PUT'
        scope = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        roleAssignmentId = uuid.uuid4()
        endpoint = f'{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentId}?api-version=2015-07-01'
        roleDefinitionId = roleDefinitionId
        params = None
        payload = {
            "properties": {
                "roleDefinitionId": f"/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId}",
                "principalId": f'{principalId}'
            }
        }
        data = http_get(method, endpoint, params, payload, self.token_management)

    def populateTypes(self, accountName):
        print(' - Creating custom type definitions...')
        with importlib.resources.path("purviewcli.ninja", "typedefs_custom.json") as filepath:
            method = 'POST'
            endpoint = f'https://{accountName}.catalog.purview.azure.com/api/atlas/v2/types/typedefs'
            params = None
            with open(filepath) as f:
                payload = json.load(f)
            data = http_get(method, endpoint, params, payload, self.token_purview)

    def populateEntities(self, accountName, args):
        # 1. Read entities.json
        with importlib.resources.path("purviewcli.ninja", "entities.json") as filepath:
            with open(filepath) as f:
                entities = json.load(f)

        # 2. Generate entities_min_rels.json
        entities_min_rels = []
        item = {}
        guid = 0
        oldGuidToNegativeGuid = {}
        for entity in entities:
            guid -= 1
            old_guid = entity['guid']
            oldGuidToNegativeGuid[old_guid] = guid
            item = {
                'guid': guid,
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
                    if classification['typeName'].startswith("Microsoft.Label") == False:
                        item['classifications'].append({ 
                            'typeName': classification['typeName'],
                            'entityStatus': classification['entityStatus'],
                        })
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
                'guid': entity['guid']
            }
            item['attributes'].pop('inputs', None)
            item['attributes'].pop('outputs', None)
            if 'classifications' in entity:
                item['classifications'] = entity['classifications']
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

        # 5. Bulk Create Entities (without relationships)
        guid_mapping = {}
        collections = [entities_primary, entities_secondary]
        print(f' - Creating entities...')
        for collection in collections:
            method = 'POST'
            endpoint = f'https://{accountName}.catalog.purview.azure.com/api/atlas/v2/entity/bulk'
            params = None
            payload = collection
            guidAssignments = http_get(method, endpoint, params, payload, self.token_purview)
            for negativeGuid in guidAssignments['guidAssignments']:
                new_guid = guidAssignments['guidAssignments'][negativeGuid]
                guid_mapping[negativeGuid] = new_guid

        # 6. Generate entities_min_rels_new.json (with new GUIDs)
        peopleFile = args['--people-file']
        users = []
        if peopleFile:
            with open(peopleFile) as f:
                people = json.load(f)
            for person in people['value']:
                users.append(person['id'])

        entities_min_rels_new = { "entities": [] }
        for entity in entities_min_rels:
            # Inputs/Outputs
            for attribute in entity['attributes']:
                if attribute == 'inputs' or attribute == 'outputs':
                    for io in entity['attributes'][attribute]:
                        if 'guid' in io:
                            negativeGuid = oldGuidToNegativeGuid[io['guid']]
                            io['guid'] = guid_mapping[f"{negativeGuid}"]
            # Relationships
            for relationshipAttribute in entity['relationshipAttributes']:
                attr = entity['relationshipAttributes'][relationshipAttribute]
                isList = True if type(attr) is list else False
                if isList:
                    for element in attr:
                        negativeGuid = oldGuidToNegativeGuid[element['guid']]
                        element['guid'] = guid_mapping[f"{negativeGuid}"]
                        element.pop('relationshipGuid', None)
                else:
                    negativeGuid = oldGuidToNegativeGuid[attr['guid']]
                    attr['guid'] = guid_mapping[f"{negativeGuid}"]
                    attr.pop('relationshipGuid', None)
            
            # Contacts
            if 'contacts' in entity:
                if len(users) > 0:
                    for key in entity['contacts']:
                        for contact in entity['contacts'][key]:
                            contact['id'] = random.choice(users)
                else:
                    entity.pop('contacts', None)

            # Pop GUID
            entity.pop('guid', None)
            entities_min_rels_new['entities'].append(entity)

        # 8. Bulk Create Entities (with relationships)
        method = 'POST'
        endpoint = f'https://{accountName}.catalog.purview.azure.com/api/atlas/v2/entity/bulk'
        params = None
        payload = entities_min_rels_new
        data = http_get(method, endpoint, params, payload, self.token_purview)

    def populateSources(self, accountName):
        print(f' - Creating sources...')
        with importlib.resources.path("purviewcli.ninja", "sources.json") as filepath:
            with open(filepath) as f:
                sources = json.load(f)

        for source in sources:
            dataSourceName = source['name']
            method = 'PUT'
            endpoint = f'https://{accountName}.scan.purview.azure.com/datasources/{dataSourceName}'
            params = None
            payload = source
            data = http_get(method, endpoint, params, payload, self.token_purview)

    def demoGenerate(self, args):
        # Init variables
        resourceGroupName = args['--resourceGroupName']
        subscriptionId = args['--subscriptionId']
        location = args['--location']

        # Start Timestamp
        startTime = datetime.now()

        # Provision Resources
        resourceGroupName = self.provisionResourceGroup(subscriptionId, location, resourceGroupName)
        accountName = self.provisionAccount(subscriptionId, location, resourceGroupName)

        # Add Role Assignment (Owner)
        roleDefinitionId = '18d7d88d-d35e-4fb5-a5c3-7773c20a72d9' # User Access Administrator
        self.assignRole(subscriptionId, resourceGroupName, accountName, roleDefinitionId)
        
        # Populate account
        print('Populating environment...')
        self.populateTypes(accountName)
        self.populateEntities(accountName, args)
        self.populateSources(accountName)
        
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
