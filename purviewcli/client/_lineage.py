from .endpoint import Endpoint, decorator, get_json


class Lineage(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def lineageRead(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/lineage/{args["--guid"]}'
        self.params = {
            'depth': args.get('--depth', 3),
            'width': args.get('--width', 6),
            'direction': args.get('--direction', 'BOTH'),
            'forceNewApi': 'true',
            'includeParent': 'true',
            'getDerivedLineage': 'true'
        }
    
    @decorator
    def lineageReadNext(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/lineage/{args["--guid"]}/next/'
        self.params = {
          'direction': args['--direction'],
          'getDerivedLineage': 'true',
          'offset': args['--offset'],
          'limit': args['--limit'],
        }

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def lineageReadUniqueAttributeType(self, args):
    #   self.method = 'GET'
    #   self.endpoint = f'/api/atlas/v2/lineage/uniqueAttribute/type/{args["--typeName"]}'
    #   self.params = {
    #     'depth': args.get('--depth', 3),
    #     'direction': args.get('--direction', 'BOTH')
    #   }
