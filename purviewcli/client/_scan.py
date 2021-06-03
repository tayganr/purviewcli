from .client import get_data, get_json

def decorator(func):
    def wrapper(self, args):
        func(self, args)
        http_dict = {'app': self.app, 'method': self.method, 'endpoint': self.endpoint, 'params': self.params, 'payload': self.payload}
        data = get_data(http_dict)
        return data
    return wrapper

class Scan:

    def __init__(self):
        self.app = 'scan'
        self.method = None
        self.endpoint = None
        self.params = None
        self.payload = None

    # ---------------------------
    # SCAN
    # ---------------------------

    # GET
    def scanReadClassificationRule(args):
        classificationRuleName = args['--classificationRuleName']
        endpoint = f'/classificationrules/{classificationRuleName}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadClassificationRules(args):
        endpoint = '/classificationrules'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadClassificationRuleVersions(args):
        classificationRuleName = args['--classificationRuleName']
        endpoint = f'/classificationrules/{classificationRuleName}/versions'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadDatasource(args):
        dataSourceName = args['--dataSourceName']
        endpoint = f'/datasources/{dataSourceName}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadDatasources(args):
        endpoint = '/datasources'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadFilters(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/filters/custom'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadKeyVault(args):
        keyVaultName = args['--keyVaultName']
        endpoint = f'/azureKeyVaults/{keyVaultName}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadKeyVaults(args):
        endpoint = '/azureKeyVaults'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadScanHistory(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/runs'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    @decorator
    def scanReadScanRuleset(self, args):
        self.method = 'GET'
        self.endpoint = f'/scanrulesets/{args["--scanRulesetName"]}'

    @decorator
    def scanReadScanRulesets(self, args):
        self.method = 'GET'
        self.endpoint = '/scanrulesets'

    def scanReadScan(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadScans(args):
        dataSourceName = args['--dataSourceName']
        endpoint = f'/datasources/{dataSourceName}/scans'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadSystemScanRuleset(args):
        dataSourceType = args['--dataSourceType']
        endpoint = f'/systemScanRulesets/datasources/{dataSourceType}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadSystemScanRulesetVersion(args):
        version = args['--version']
        dataSourceType = args['--dataSourceType']
        endpoint = f'/systemScanRulesets/versions/{version}?dataSourceType={dataSourceType}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadSystemScanRulesetLatest(args):
        dataSourceType = args['--dataSourceType']
        endpoint = f'/systemScanRulesets/versions/latest?dataSourceType={dataSourceType}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadSystemScanRulesets(args):
        endpoint = '/systemScanRulesets'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadSystemScanRulesetVersions(args):
        dataSourceType = args['--dataSourceType']
        endpoint = f'/systemScanRulesets/versions?dataSourceType={dataSourceType}'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanReadTrigger(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/triggers/default'
        http_dict = {'app': 'scan', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    # DELETE
    @decorator
    def scanDeleteClassificationRule(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/classificationrules/{args["--classificationRuleName"]}'

    def scanDeleteDataSource(args):
        dataSourceName = args['--dataSourceName']
        endpoint = f'/datasources/{dataSourceName}'
        http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanDeleteKeyVault(args):
        keyVaultName = args['--keyVaultName']
        endpoint = f'/azureKeyVaults/{keyVaultName}'
        http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanDeleteScanRuleset(args):
        scanRulesetName = args['--scanRulesetName']
        endpoint = f'/scanrulesets/{scanRulesetName}'
        http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanDeleteScan(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}'
        http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanDeleteTrigger(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/triggers/default'
        http_dict = {'app': 'scan', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    # PUT
    def scanPutClassificationRule(args):
        classificationRuleName = args['--classificationRuleName']
        endpoint = f'/classificationrules/{classificationRuleName}'
        payload = get_json(args,'--payload-file')
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
        data = get_data(http_dict)
        return data

    def scanPutDataSource(args):
        dataSourceName = args['--dataSourceName']
        endpoint = f'/datasources/{dataSourceName}'
        payload = get_json(args,'--payload-file')
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
        data = get_data(http_dict)
        return data

    def scanPutFilter(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/filters/custom'
        payload = get_json(args,'--payload-file')
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
        data = get_data(http_dict)
        return data

    def scanPutKeyVault(args):
        keyVaultName = args['--keyVaultName']
        endpoint = f'/azureKeyVaults/{keyVaultName}'
        payload = get_json(args,'--payload-file')
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
        data = get_data(http_dict)
        return data

    def scanRunScan(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        runId = args['--runId']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/runs/{runId}'
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': None}
        data = get_data(http_dict)
        return data

    def scanPutScanRuleset(args):
        scanRulesetName = args['--scanRulesetName']
        endpoint = f'/scanrulesets/{scanRulesetName}'
        payload = get_json(args,'--payload-file')
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
        data = get_data(http_dict)
        return data

    @decorator
    def scanPutScan(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}'
        self.payload = get_json(args,'--payload-file')

    def scanPutTrigger(args):
        dataSourceName = args['--dataSourceName']
        scanName = args['--scanName']
        endpoint = f'/datasources/{dataSourceName}/scans/{scanName}/triggers/default'
        payload = get_json(args,'--payload-file')
        http_dict = {'app': 'scan', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
        data = get_data(http_dict)
        return data
