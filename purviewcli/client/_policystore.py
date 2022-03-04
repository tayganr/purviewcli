from .endpoint import Endpoint, decorator, get_json

class Policystore(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'policystore'

    # Metadata Policies
    @decorator
    def policystoreReadMetadataRoles(self, args):
        self.method = 'GET'
        self.endpoint = '/metadataroles'
        self.params = {"api-version": "2021-07-01"}

    @decorator
    def policystoreReadMetadataPolicy(self, args):
        self.method = 'GET'
        self.endpoint = f'/collections/{args["--collectionName"]}/metadataPolicy' if args["--policyId"] is None else f'/metadataPolicies/{args["--policyId"]}'
        self.params = {"api-version": "2021-07-01"}

    @decorator
    def policystoreReadMetadataPolicies(self, args):
        self.method = 'GET'
        self.endpoint = '/metadataPolicies'
        self.params = {"api-version": "2021-07-01"}

    @decorator
    def policystorePutMetadataPolicy(self, args):
        self.method = 'PUT'
        self.endpoint = f'/metadataPolicies/{args["--policyId"]}'
        self.params = {"api-version": "2021-07-01"}
        self.payload = get_json(args, '--payloadFile')

    # Data Policies
    @decorator
    def policystoreReadDataPolicies(self, args):
        policyName = args['--policyName']
        self.method = 'GET'
        self.endpoint = f'/dataPolicies/{policyName}' if args['--policyName'] else '/dataPolicies'
        self.params = {'api-version': '2021-01-01-preview'}

    @decorator
    def policystorePutDataPolicy(self, args):
        policyName = args['--policyName']
        self.method = 'PUT'
        self.endpoint = f'/dataPolicies/{policyName}'
        self.params = {'api-version': '2021-01-01-preview'}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def policystoreReadDataPolicyScopes(self, args):
        policyName = args['--policyName']
        self.method = 'GET'
        self.endpoint = f'/dataPolicies/{policyName}/scopes'
        self.params = {'api-version': '2021-01-01-preview'}

    @decorator
    def policystorePutDataPolicyScope(self, args):
        policyName = args['--policyName']
        self.method = 'PUT'
        self.endpoint = f'/dataPolicies/{policyName}/scopes'
        self.params = {'api-version': '2021-01-01-preview'}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def policystoreDeleteDataPolicyScope(self, args):
        policyName = args['--policyName']
        datasource = args['--datasource']
        self.method = 'DELETE'
        self.endpoint = f'/dataPolicies/{policyName}/scopes/{datasource}'
        self.params = {'api-version': '2021-01-01-preview'}

    @decorator
    def policystoreDeleteDataPolicy(self, args):
        policyName = args['--policyName']
        self.method = 'DELETE'
        self.endpoint = f'/dataPolicies/{policyName}'
        self.params = {'api-version': '2021-01-01-preview'}
