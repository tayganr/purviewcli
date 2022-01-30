from .endpoint import Endpoint, decorator, get_json
import random
import string

def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return result_str

class Account(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'account'

    @decorator
    def accountGetAccount(self, args):
        self.method = 'GET'
        self.endpoint = '/'
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountUpdateAccount(self, args):
        self.method = 'PATCH'
        self.endpoint = '/'
        self.params = {"api-version": "2019-11-01-preview"}
        self.payload = {
            "friendlyName": f"{args['--friendlyName']}"
        }

    @decorator
    def accountGetCollections(self, args):
        self.method = 'GET'
        self.endpoint = '/collections'
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountGetCollection(self, args):
        self.method = 'GET'
        self.endpoint = f"/collections/{args['--collectionName']}"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountGetCollectionPath(self, args):
        self.method = 'GET'
        self.endpoint = f"/collections/{args['--collectionName']}/getCollectionPath"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountGetChildCollectionNames(self, args):
        self.method = 'GET'
        self.endpoint = f"/collections/{args['--collectionName']}/getChildCollectionNames"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountDeleteCollection(self, args):
        self.method = 'DELETE'
        self.endpoint = f"/collections/{args['--collectionName']}"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountPutCollection(self, args):
        collectionName = get_random_string(6)
        self.method = 'PUT'
        self.endpoint = f"/collections/{collectionName}"
        self.params = {"api-version": "2019-11-01-preview"}
        self.payload = {
            "friendlyName": f"{args['--friendlyName']}",
            "name": f"{collectionName}",
            "parentCollection": {
                "referenceName": f"{args['--parentCollection']}",
                "type": "CollectionReference"
            }
        }

    @decorator
    def accountGetAccessKeys(self, args):
        self.method = 'POST'
        self.endpoint = f"/listkeys"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountRegenerateAccessKeys(self, args):
        self.method = 'POST'
        self.endpoint = f"/regeneratekeys"
        self.params = {"api-version": "2019-11-01-preview"}
        self.payload = {
            "keyType": f"{args['--keyType']}"
        }

    @decorator
    def accountGetResourceSetRules(self, args):
        self.method = 'GET'
        self.endpoint = f"/resourceSetRuleConfigs"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountDeleteResourceSetRule(self, args):
        self.method = 'DELETE'
        self.endpoint = f"/resourceSetRuleConfigs/defaultResourceSetRuleConfig"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountGetResourceSetRule(self, args):
        self.method = 'GET'
        self.endpoint = f"/resourceSetRuleConfigs/defaultResourceSetRuleConfig"
        self.params = {"api-version": "2019-11-01-preview"}

    @decorator
    def accountPutResourceSetRule(self, args):
        self.method = 'PUT'
        self.endpoint = f"/resourceSetRuleConfigs/defaultResourceSetRuleConfig"
        self.params = {"api-version": "2019-11-01-preview"}
        self.payload = get_json(args, '--payloadFile')
