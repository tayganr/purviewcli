from .client import get_data

# ---------------------------
# SCAN
# ---------------------------
def scanReadSources(args):
    endpoint = '/datasources'
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadSource(args):
    endpoint = '/datasources/%s' % args['--datasource']
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadScans(args):
    endpoint = '/datasources/%s/scans' % args['--datasource']
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanRead(args):
    endpoint = '/datasources/%s/scans/%s' % (args['--datasource'], args['--scanName'])
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadHistory(args):
    endpoint = '/datasources/%s/scans/%s/listHistory' % (args['--datasource'], args['--scanName'])
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadFilters(args):
    endpoint = '/datasources/%s/scans/%s/filters' % (args['--datasource'], args['--scanName'])
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanRun(args):
    endpoint = '/datasources/%s/scans/%s/run' % (args['--datasource'], args['--scanName'])

    if args['--scanLevel']:
        payload = {'scanLevel': args['--scanLevel']}
    else:
        payload = None
    
    http_dict = {'app': 'scan', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def scanReadScanRulesets(args):
    endpoint = '/scanrulesets'
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadSystemScanRulesets(args):
    endpoint = '/systemScanRulesets'
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadSystemScanRulesetsSettings(args):
    endpoint = '/systemScanRulesets/settings'
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadClassificationRules(args):
    endpoint = '/classificationrules'
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanReadClassificationRule(args):
    endpoint = '/classificationrules/%s' % args['--classificationName']
    http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanCreateCollection(args):
    endpoint = '/datasources/%s' % args['--collection']
    payload = {
        "kind": "Collection",
        "name": args['--collection'],
        "properties": {}
    }
    if args['--parentCollection']:
        payload['properties'] = {
            "parentCollection": {
                "type":"DataSourceReference",
                "referenceName": args['--parentCollection']
            }
        }
    http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def scanDeleteCollection(args):
    endpoint = '/datasources/%s' % args['--collection']
    http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data

def scanCreateSource(args):
    endpoint = '/datasources/%s' % args['--datasource']
    payload = {
        "kind": args['--kind'],
        "name": args['--datasource'],
        "properties": {}
    }
    
    # Source Properties
    if args['--kind'] == 'AzureCosmosDb':
        payload['properties'] = {
            "accountUri": args['--accountUri'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AzureDataExplorer':
        payload['properties'] = {
            "endpoint": args['--endpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AdlsGen1':
        payload['properties'] = {
            "endpoint": args['--endpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AdlsGen2':
        payload['properties'] = {
            "endpoint": args['--endpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AzureStorage':
        payload['properties'] = {
            "endpoint": args['--endpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AzureSqlDatabase':
        payload['properties'] = {
            "serverEndpoint": args['--serverEndpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AzureSqlDataWarehouse':
        payload['properties'] = {
            "serverEndpoint": args['--serverEndpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'PowerBI':
        payload['properties'] = {
            "tenant": args['--tenant']
        }
    elif args['--kind'] == 'SqlServerDatabase':
        payload['properties'] = {
            "serverEndpoint": args['--serverEndpoint']
        }
    elif args['--kind'] == 'AzureSqlDatabaseManagedInstance':
        payload['properties'] = {
            "serverEndpoint": args['--serverEndpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'AzureFileService':
        payload['properties'] = {
            "endpoint": args['--endpoint'],
            "subscriptionId": args['--subscriptionId'],
            "resourceGroup": args['--resourceGroup'],
            "location": args['--location'],
            "resourceName": args['--resourceName'][0]
        }
    elif args['--kind'] == 'Teradata':
        payload['properties'] = {
            "host": args['--host']
        }
    elif args['--kind'] == 'SapEcc':
        payload['properties'] = {
            "applicationServer": args['--applicationServer'],
            "systemNumber": args['--systemNumber']
        }
    elif args['--kind'] == 'SapS4Hana':
        payload['properties'] = {
            "applicationServer": args['--applicationServer'],
            "systemNumber": args['--systemNumber']
        }
    elif args['--kind'] == 'Hive':
        payload['properties'] = {
            "clusterUrl": args['--clusterUrl'],
            "host": args['--host']
        }
    elif args['--kind'] == 'AmazonS3':
        payload['properties'] = {
            "roleARN": args['--roleARN'],
            "serviceUrl": args['--serviceUrl']
        }

    else:
        pass

    if args['--parentCollection']:
        payload['properties']['parentCollection'] = {
            "type":"DataSourceReference",
            "referenceName": args['--parentCollection']
        }
    http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def scanDeleteSource(args):
    endpoint = '/datasources/%s' % args['--datasource']
    http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data