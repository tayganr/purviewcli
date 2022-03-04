import uuid
from .endpoint import Endpoint, decorator, get_json

class Scan(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'scan'

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
    def scanReadDataSource(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}'

    @decorator
    def scanReadDataSources(self, args):
        collectionName = args['--collectionName']
        self.method = 'GET'
        self.endpoint = f'/collections/{collectionName}/listDataSources' if args['--collectionName'] else '/datasources'

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
        self.endpoint = f'/systemScanRulesets/versions/{args["--version"]}'
        self.params = {'dataSourceType': args["--dataSourceType"]}

    @decorator
    def scanReadSystemScanRulesetLatest(self, args):
        self.method = 'GET'
        self.endpoint = f'/systemScanRulesets/versions/latest'
        self.params = {'dataSourceType': args["--dataSourceType"]}

    @decorator
    def scanReadSystemScanRulesets(self, args):
        self.method = 'GET'
        self.endpoint = '/systemScanRulesets'

    @decorator
    def scanReadSystemScanRulesetVersions(self, args):
        self.method = 'GET'
        self.endpoint = f'/systemScanRulesets/versions'
        self.params = {'dataSourceType': args["--dataSourceType"]}

    @decorator
    def scanReadTrigger(self, args):
        self.method = 'GET'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/triggers/default'

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

    @decorator
    def scanPutClassificationRule(self, args):
        self.method = 'PUT'
        self.endpoint = f'/classificationrules/{args["--classificationRuleName"]}'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanPutDataSource(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanPutFilter(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/filters/custom'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanPutKeyVault(self, args):
        self.method = 'PUT'
        self.endpoint = f'/azureKeyVaults/{args["--keyVaultName"]}'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanRunScan(self, args):
        self.method = 'POST'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/run'
        self.params = {"api-version": "2018-12-01-preview"}
        self.payload = {"scanLevel": args["--scanLevel"] }
        self.headers = {'Content-Type':'application/json'}
    
    @decorator
    def scanCancelScan(self, args):
        self.method = 'POST'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/runs/{args["--runId"]}/:cancel'

    @decorator
    def scanPutScanRuleset(self, args):
        self.method = 'PUT'
        self.endpoint = f'/scanrulesets/{args["--scanRulesetName"]}'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanPutScan(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanPutTrigger(self, args):
        self.method = 'PUT'
        self.endpoint = f'/datasources/{args["--dataSourceName"]}/scans/{args["--scanName"]}/triggers/default'
        self.payload = get_json(args,'--payloadFile')

    @decorator
    def scanTagClassificationVersion(self, args):
        self.method = 'POST'
        self.endpoint = f"/classificationrules/{args['--classificationRuleName']}/versions/{args['--classificationRuleVersion']}/:tag"
        self.params = {
            "action": f"{args['--action']}",
            "api-version": "2018-12-01-preview"
        }

    # Credential
    @decorator
    def scanReadCredential(self, args):
        self.method = 'GET'
        self.endpoint = '/credentials' if args["--credentialName"] is None else f'/credentials/{args["--credentialName"]}'
        self.params = {"api-version": "2018-12-01-preview"}

    @decorator
    def scanPutCredential(self, args):
        self.method = 'PUT'
        self.endpoint = f'/credentials/{args["--credentialName"]}'
        self.payload = get_json(args, '--payloadFile')
        self.params = {"api-version": "2018-12-01-preview"}

    @decorator
    def scanDeleteCredential(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/credentials/{args["--credentialName"]}'
        self.params = {"api-version": "2018-12-01-preview"}