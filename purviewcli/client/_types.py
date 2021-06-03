from .endpoint import Endpoint, decorator, get_json

class Types(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def typesReadBusinessmetadatadef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/businessmetadatadef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadClassificationdef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/classificationdef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadEntitydef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/entitydef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadEnumdef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/enumdef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadRelationshipdef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/relationshipdef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadStructdef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/structdef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadTypedef(self, args):
        self.method = 'GET'
        typeDefKey = 'guid' if args['--name'] is None else 'name'
        typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
        self.endpoint = f'/api/atlas/v2/types/typedef/{typeDefKey}/{typeDefVal}'

    @decorator
    def typesReadTypedefs(self, args):
        self.method = 'GET'
        self.endpoint = '/api/atlas/v2/types/typedefs'
        self.params = {'includeTermTemplate': str(args["--includeTermTemplate"]).lower()}
        self.params['type'] = args["--type"] if args["--type"] else None

    @decorator
    def typesReadTypedefsHeaders(self, args):
      self.method = 'GET'
      self.endpoint = '/api/atlas/v2/types/typedefs/headers'
      self.params = {'includeTermTemplate': str(args["--includeTermTemplate"]).lower()}
      self.params['type'] = args["--type"] if args["--type"] else None

    @decorator
    def typesDeleteTypedef(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/types/typedef/name/{args["--name"]}'

    @decorator
    def typesDeleteTypedefs(self, args):
        self.method = 'DELETE'
        self.endpoint = '/api/atlas/v2/types/typedefs'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def typesCreateTypedefs(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/types/typedefs'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def typesPutTypedefs(self, args):
        self.method = 'PUT'
        self.endpoint = '/api/atlas/v2/types/typedefs'
        self.payload = get_json(args, '--payload-file')
