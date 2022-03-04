from .endpoint import Endpoint, decorator, get_json

class Policystore(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'base'

    # Metadata Policies
    @decorator
    def policystoreReadMetadataRoles(self, args):
        self.method = 'GET'
        self.endpoint = '/policystore/metadataroles'
        self.params = {"api-version": "2021-07-01"}

    @decorator
    def policystoreReadMetadataPolicy(self, args):
        self.method = 'GET'
        self.endpoint = f'/policystore/collections/{args["--collectionName"]}/metadataPolicy' if args["--policyId"] is None else f'/policystore/metadataPolicies/{args["--policyId"]}'
        self.params = {"api-version": "2021-07-01"}

    @decorator
    def policystoreReadMetadataPolicies(self, args):
        self.method = 'GET'
        self.endpoint = '/policystore/metadataPolicies'
        self.params = {"api-version": "2021-07-01"}

    @decorator
    def policystorePutMetadataPolicy(self, args):
        self.method = 'PUT'
        self.endpoint = f'/policystore/metadataPolicies/{args["--policyId"]}'
        self.params = {"api-version": "2021-07-01"}
        self.payload = get_json(args, '--payloadFile')

    # Data Policies
    @decorator
    def policystoreReadDataPolicies(self, args):
        policyName = args['--policyName']
        self.method = 'GET'
        self.endpoint = f'/policystore/dataPolicies/{policyName}' if args['--policyName'] else '/policystore/dataPolicies'
        self.params = {'api-version': '2021-01-01-preview'}

    @decorator
    def policystorePutDataPolicy(self, args):
        policyName = args['--policyName']
        self.method = 'PUT'
        self.endpoint = f'/policystore/dataPolicies/{policyName}'
        self.params = {'api-version': '2021-01-01-preview'}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def policystoreReadDataPolicyScopes(self, args):
        policyName = args['--policyName']
        self.method = 'GET'
        self.endpoint = f'/policystore/dataPolicies/{policyName}/scopes'
        self.params = {'api-version': '2021-01-01-preview'}

    @decorator
    def policystorePutDataPolicyScope(self, args):
        policyName = args['--policyName']
        self.method = 'PUT'
        self.endpoint = f'/policystore/dataPolicies/{policyName}/scopes'
        self.params = {'api-version': '2021-01-01-preview'}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def policystoreDeleteDataPolicyScope(self, args):
        policyName = args['--policyName']
        scopeName = args['--scopeName']
        self.method = 'DELETE'
        self.endpoint = f'/policystore/dataPolicies/{policyName}/scopes/{scopeName}'
        self.params = {'api-version': '2021-01-01-preview'}

    @decorator
    def policystoreDeleteDataPolicy(self, args):
        policyName = args['--policyName']
        self.method = 'DELETE'
        self.endpoint = f'/policystore/dataPolicies/{policyName}'
        self.params = {'api-version': '2021-01-01-preview'}
