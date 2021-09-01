from .endpoint import Endpoint, decorator, get_json

class Policystore(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'base'

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
        self.payload = get_json(args, '--payload-file')
