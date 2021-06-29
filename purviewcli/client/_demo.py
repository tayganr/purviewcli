import time, json, string, random
from os import read
from subprocess import Popen, PIPE
from purviewcli.client import settings

def runCommand(cmd):
    print('calling')
    output = Popen(cmd.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0].decode('ascii')
    output = json.loads(output)
    return output


class Demo():
    def demoGenerate(self, args):
        # Init variables
        accountName = None
        nameAvailable = False

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
        print('[WORKING] Provisioning Azure Purview account...')
        cmd = f"pv management createAccount --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --accountName {accountName} --payload-file temp.json"
        data = runCommand(cmd)

        # Check provisioningState until Succeeded
        provisioning = True
        while provisioning:
            time.sleep(30)
            cmd = f"pv management readAccount --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --accountName {accountName}"
            data = runCommand(cmd)
            if data['properties']['provisioningState'] == 'Succeeded':
                provisioning = False

        catalogEndpoint = data['properties']['endpoints']['catalog']

        # output = !pv types createTypeDefs --payload-file "{source_path}/types/typedefs_custom.json"
        # # Map qualifiedName to OLD GUID
        # with open(f"{source_path}/entities/entities.json") as f:
        #     original_entities = json.load(f)

        # old_entities = {}
        # for entity in original_entities:
        #     qualifiedName = entity['attributes']['qualifiedName']
        #     old_guid = entity['guid']
        #     old_entities[qualifiedName] = old_guid

        # # Create Entities
        # guid_mapping = {}
        # filepaths = [f"{source_path}/entities/entities_min1.json", f"{source_path}/entities/entities_min2.json"]

        # for filepath in filepaths:
        #     print(f'[WORKING] Creating entities from {filepath}...')
        #     guidAssignments = !pv entity createBulk --payload-file {filepath}
        #     guidAssignments = getJSON(guidAssignments)

        #     # Map OLD GUID to NEW GUID
        #     with open(filepath) as f:
        #         entities = json.load(f)

        #     counter = 0
        #     for entity in entities['entities']:
        #         new_guid = list(guidAssignments['guidAssignments'].items())[counter][1]
        #         qualifiedName = entity['attributes']['qualifiedName']
        #         old_guid = old_entities[qualifiedName]
        #         guid_mapping[old_guid] = new_guid
        #         counter += 1
        # print('[COMPLETE] Bulk creation of entities complete!')

        # # Replace references to OLD GUID with NEW GUID
        # with open(f"{source_path}/entities/entities_rels_old.json") as f:
        #     entities_with_rels = json.load(f)

        # for entity in entities_with_rels['entities']:
        #     # Inputs/Outputs
        #     for attribute in entity['attributes']:
        #         if attribute == 'inputs' or attribute == 'outputs':
        #             for io in entity['attributes'][attribute]:
        #                 if 'guid' in io:
        #                     old_guid = io['guid']
        #                     io['guid'] = guid_mapping[old_guid]
        #     # Relationships
        #     for relationshipAttribute in entity['relationshipAttributes']:
        #         attr = entity['relationshipAttributes'][relationshipAttribute]
        #         isList = True if type(attr) is list else False
        #         if isList:
        #             for element in attr:
        #                 old_guid = element['guid']
        #                 element['guid'] = guid_mapping[old_guid]
        #                 element.pop('relationshipGuid', None)
        #         else:
        #             old_guid = attr['guid']
        #             attr['guid'] = guid_mapping[old_guid]
        #             attr.pop('relationshipGuid', None)

        # # Export updated entities with relationships JSON document
        # from pathlib import Path
        # directory = f"{source_path}/relationships"
        # Path(directory).mkdir(parents=True, exist_ok=True)

        # filepath = f'{directory}/entities_rels_new.json'
        # with open(filepath, 'w') as fp:
        #     json.dump(entities_with_rels, fp, indent=4, sort_keys=True)

        # print(f'[WORKING] Creating entities with relationships from {filepath}...')
        # output = !pv entity createBulk --payload-file {filepath}
        # print('[COMPLETE] Bulk creation of entities with relationships complete!')

        response = { 'x': 'y' }
        return response
