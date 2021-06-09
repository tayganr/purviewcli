from .endpoint import Endpoint, decorator, get_json

class Credential(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'proxy'

    @decorator
    def credentialRead(self, args):
        self.method = 'GET'
        self.endpoint = '/credentials' if args["--credentialName"] is None else f'/credentials/{args["--credentialName"]}'
        self.params = {"api-version": "2020-12-01-preview"}

    @decorator
    def credentialPut(self, args):
        self.method = 'PUT'
        self.endpoint = f'/credentials/{args["--credentialName"]}'
        self.payload = get_json(args, '--payload-file')
        self.params = {"api-version": "2020-12-01-preview"}

    @decorator
    def credentialDelete(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/credentials/{args["--credentialName"]}'
        self.params = {"api-version": "2020-12-01-preview"}
