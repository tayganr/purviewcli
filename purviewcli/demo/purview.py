import json, random, importlib.resources, uuid
from purviewcli.demo.utils import http_get

class DataPlane():
    def __init__(self):
        self.token = None

    def registerSource(self, accountName, dataSourceName, payload):
        method = 'PUT'
        endpoint = f'https://{accountName}.scan.purview.azure.com/datasources/{dataSourceName}'
        params = None
        data = http_get(method, endpoint, params, payload, self.token)
        return data
    
    def createScan(self, accountName, dataSourceName, scanName, payload):
        method = 'PUT'
        endpoint = f'https://{accountName}.scan.purview.azure.com/datasources/{dataSourceName}/scans/{scanName}'
        params = None
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    def runScan(self, accountName, dataSourceName, scanName):
        method = 'PUT'
        endpoint = f'https://{accountName}.scan.purview.azure.com/datasources/{dataSourceName}/scans/{scanName}/runs/{str(uuid.uuid4())}'
        params = None
        payload = None
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    def populateTypes(self, accountName):
        print(' - Creating custom type definitions...')
        with importlib.resources.path("purviewcli.ninja", "typedefs_custom.json") as filepath:
            with open(filepath) as f:
                typedefs = json.load(f)
        method = 'POST'
        endpoint = f'https://{accountName}.catalog.purview.azure.com/api/atlas/v2/types/typedefs'
        params = None
        payload = typedefs
        data = http_get(method, endpoint, params, payload, self.token)

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
            data = http_get(method, endpoint, params, payload, self.token)

    def populateEntities(self, accountName, peopleFile):
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
            guidAssignments = http_get(method, endpoint, params, payload, self.token)
            for negativeGuid in guidAssignments['guidAssignments']:
                new_guid = guidAssignments['guidAssignments'][negativeGuid]
                guid_mapping[negativeGuid] = new_guid

        # 6. Generate entities_min_rels_new.json (with new GUIDs)
        users = []
        if peopleFile:
            with open(peopleFile) as f:
                people = json.load(f)
            for person in people['value']:
                if person['userPrincipalName'] != None:
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
        data = http_get(method, endpoint, params, payload, self.token)
