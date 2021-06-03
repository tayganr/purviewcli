from .endpoint import Endpoint, decorator, get_json

class Relationship(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def relationshipCreate(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/relationship'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def relationshipPut(self, args):
        self.method = 'PUT'
        self.endpoint = '/api/atlas/v2/relationship'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def relationshipDelete(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/relationship/guid/{args["--guid"]}'

    @decorator
    def relationshipRead(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/relationship/guid/{args["--guid"]}'
        self.params = {'extendedInfo': str(args["--extendedInfo"]).lower()}
