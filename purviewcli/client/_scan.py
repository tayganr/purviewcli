import uuid
from .endpoint import Endpoint, decorator, get_json

class Scan(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'scan'

    # GET
    @decorator
    def scanReadClassificationRule(self, args):
        self.method = 'GET'
        self.endpoint = f'/classificationrules/{args["--classificationRuleName"]}'

    @decorator
    def scanReadClassificationRules(self, args):
        self.method = 'GET'
        self.endpoint = '/classificationrules'

    @decorator
    def scanReadClassificationRuleVersions(self, args):
        self.method = 'GET'
        self.endpoint = f'/classificationrules/{args["--classificationRuleName"]}/versions'

    @decorator
    def scanReadDatasource(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}'

    @decorator
    def scanReadDatasources(self, args):
        self.method = 'GET'
        self.endpoint = '/datasources'

    @decorator
    def scanReadFilters(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/filters/custom'

    @decorator
    def scanReadKeyVault(self, args):
        self.method = 'GET'
        self.endpoint = f'/azureKeyVaults/{args["--keyVaultName"]}'

    @decorator
    def scanReadKeyVaults(self, args):
        self.method = 'GET'
        self.endpoint = '/azureKeyVaults'

    @decorator
    def scanReadScanHistory(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/runs'

    @decorator
    def scanReadScanRuleset(self, args):
        self.method = 'GET'
        self.endpoint = f'/scanrulesets/{args["--scanRulesetName"]}'

    @decorator
    def scanReadScanRulesets(self, args):
        self.method = 'GET'
        self.endpoint = '/scanrulesets'

    @decorator
    def scanReadScan(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}'

    @decorator
    def scanReadScans(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans'

    @decorator
    def scanReadSystemScanRuleset(self, args):
        self.method = 'GET'
        self.endpoint = f'/systemScanRulesets/datasources/{args["--dataSourceType"]}'

    @decorator
    def scanReadSystemScanRulesetVersion(self, args):
        self.method = 'GET'
        self.endpoint = f'/systemScanRulesets/versions/{args["--version"]}?dataSourceType={args["--dataSourceType"]}'

    @decorator
    def scanReadSystemScanRulesetLatest(self, args):
        self.method = 'GET'
        self.endpoint = f'/systemScanRulesets/versions/latest?dataSourceType={args["--dataSourceType"]}'

    @decorator
    def scanReadSystemScanRulesets(self, args):
        self.method = 'GET'
        self.endpoint = '/systemScanRulesets'

    @decorator
    def scanReadSystemScanRulesetVersions(self, args):
        self.method = 'GET'
        self.endpoint = f'/systemScanRulesets/versions?dataSourceType={args["--dataSourceType"]}'

    @decorator
    def scanReadTrigger(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/triggers/default'

    # DELETE
    @decorator
    def scanDeleteClassificationRule(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/classificationrules/{args["--classificationRuleName"]}'

    @decorator
    def scanDeleteDataSource(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}'

    @decorator
    def scanDeleteKeyVault(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/azureKeyVaults/{args["--keyVaultName"]}'

    @decorator
    def scanDeleteScanRuleset(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/scanrulesets/{args["--scanRulesetName"]}'

    @decorator
    def scanDeleteScan(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}'

    @decorator
    def scanDeleteTrigger(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/triggers/default'

    # PUT
    @decorator
    def scanPutClassificationRule(self, args):
        self.method = 'PUT'
        self.endpoint = f'/classificationrules/{args["--classificationRuleName"]}'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def scanPutDataSource(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def scanPutFilter(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/filters/custom'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def scanPutKeyVault(self, args):
        self.method = 'PUT'
        self.endpoint = f'/azureKeyVaults/{args["--keyVaultName"]}'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def scanRunScan(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/runs/{str(uuid.uuid4())}'
    
    @decorator
    def scanCancelScan(self, args):
        self.method = 'POST'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/runs/{args["--runId"]}/:cancel'

    @decorator
    def scanPutScanRuleset(self, args):
        self.method = 'PUT'
        self.endpoint = f'/scanrulesets/{args["--scanRulesetName"]}'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def scanPutScan(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def scanPutTrigger(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/triggers/default'
        self.payload = get_json(args,'--payload-file')
