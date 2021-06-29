import math, time, json, string, random, importlib.resources
from datetime import datetime
from os import read
from subprocess import Popen, PIPE
from purviewcli.client import settings

def runCommand(cmd):
    # print('calling')
    output = Popen(cmd.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0].decode('ascii')
    output = json.loads(output)
    return output

class Demo():
    def demoGenerate(self, args):
        # Init variables
        accountName = None
        nameAvailable = False
        startTime = datetime.now()

        # Generate Azure Purview Account Name
        while nameAvailable == False:
            accountName = 'purview-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            cmd = f"pv management checkNameAvailability --subscriptionId {args['--subscriptionId']} --accountName {accountName}"
            data = runCommand(cmd)
            nameAvailable = data['nameAvailable']
        print(f'Account Name: {accountName}')

        # Provision Resource Group
        resourceGroupName = args['--resourceGroupName'] or 'purview-rg-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        cmd = f"pv management putResourceGroup --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --location {args['--location']}"
        data = runCommand(cmd)
        print(f'Resource Group: {resourceGroupName}')

        # Provision Azure Purview Account
        payload = {
            "identity": {
                "type": "SystemAssigned"
            },
            "location": args['--location'],
            "sku": {
                "name": "Standard",
                "capacity": 4
            }
        }
        with open('temp.json', 'w') as f:
            json.dump(payload, f)
        print('Provisioning Azure Purview account...')
        cmd = f"pv management createAccount --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --accountName {accountName} --payload-file temp.json"
        data = runCommand(cmd)

        # Check provisioningState until Succeeded
        provisioning = True
        while provisioning:
            time.sleep(30)
            # print('Checking status...')
            cmd = f"pv management readAccount --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --accountName {accountName}"
            data = runCommand(cmd)
            if data['properties']['provisioningState'] == 'Succeeded':
                provisioning = False
        
        print(f'Ready! Purview Studio: https://ms.web.purview.azure.com/resource/{accountName}')


        print('Populating environment...')

        # Create Custom Type Definitions
        print(' - Creating custom type definitions...')
        with importlib.resources.path("purviewcli.ninja.types", "typedefs_custom.json") as filepath:
            cmd = f"pv types createTypeDefs --payload-file {filepath} --purviewName {accountName}"
            data = runCommand(cmd)

        # Import original entities
        with importlib.resources.path("purviewcli.ninja.entities", "entities.json") as filepath:
            with open(filepath) as f:
                original_entities = json.load(f)

        # Map qualifiedName to OLD GUID
        old_entities = {}
        for entity in original_entities:
            qualifiedName = entity['attributes']['qualifiedName']
            old_guid = entity['guid']
            old_entities[qualifiedName] = old_guid

        # Create Entities
        guid_mapping = {}
        filepaths = []

        # Path to Primary Entities
        with importlib.resources.path("purviewcli.ninja.entities", "entities_min1.json") as filepath:
            filepaths.append(filepath)

        # Path to Secondary Entities
        with importlib.resources.path("purviewcli.ninja.entities", "entities_min2.json") as filepath:
            filepaths.append(filepath)

        # Bulk Create Entities
        for filepath in filepaths:
            print(f' - Creating entities from {filepath}...')
            cmd = f"pv entity createBulk --payload-file {filepath} --purviewName {accountName}"
            guidAssignments = runCommand(cmd)

            # Map OLD GUID to NEW GUID
            with open(filepath) as f:
                entities = json.load(f)

            counter = 0
            for entity in entities['entities']:
                new_guid = list(guidAssignments['guidAssignments'].items())[counter][1]
                qualifiedName = entity['attributes']['qualifiedName']
                old_guid = old_entities[qualifiedName]
                guid_mapping[old_guid] = new_guid
                counter += 1

        # Replace references to OLD GUID with NEW GUID
        with importlib.resources.path("purviewcli.ninja.entities", "entities_rels_old.json") as filepath:
            with open(filepath) as f:
                entities_with_rels = json.load(f)

            for entity in entities_with_rels['entities']:
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

        # Create Relationships
        with importlib.resources.path("purviewcli.ninja.relationships", "entities_rels_new.json") as filepath:
            with open(filepath, 'w') as fp:
                json.dump(entities_with_rels, fp, indent=4, sort_keys=True)

            print(f' - Creating entities with relationships from {filepath}...')
            cmd = f"pv entity createBulk --payload-file {filepath} --purviewName {accountName}"
            data = runCommand(cmd)
        
        print('[COMPLETE] Bulk creation of entities with relationships complete!')

        finishTime = datetime.now()
        duration = finishTime - startTime
        minutes = math.floor(duration.seconds / 60)
        seconds = duration.seconds % 60
        print(f'Duration: {minutes:02}:{seconds:02}')

        response = 'Hello World!'
        return response
