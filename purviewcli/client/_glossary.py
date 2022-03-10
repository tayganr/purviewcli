from .endpoint import Endpoint, decorator, get_json

class Glossary(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def glossaryRead(self, args):
        self.method = 'GET'
        self.endpoint = '/api/atlas/v2/glossary' if args["--glossaryGuid"] is None else f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort'], 'ignoreTermsAndCategories': args['--ignoreTermsAndCategories']}

    @decorator
    def glossaryCreate(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryCreateCategories(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/categories'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryCreateCategory(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/category'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryDeleteCategory(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}'

    @decorator
    def glossaryReadCategory(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryPutCategory(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryPutCategoryPartial(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}/partial'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryReadCategoryRelated(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}/related'

    @decorator
    def glossaryReadCategoryTerms(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}/terms'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryCreateTerm(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/term'
        self.payload = get_json(args, '--payloadFile')
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}

    @decorator
    def glossaryDeleteTerm(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}'

    @decorator
    def glossaryReadTerm(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}'
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}

    @decorator
    def glossaryPutTerm(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}'
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryPutTermPartial(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}/partial'
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryCreateTerms(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/terms'
        self.payload = get_json(args, '--payloadFile')
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}

    @decorator
    def glossaryDeleteTermsAssignedEntities(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryReadTermsAssignedEntities(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryCreateTermsAssignedEntities(self, args):
        self.method = 'POST'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryPutTermsAssignedEntities(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryReadTermsRelated(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/related'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryDelete(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}'

    @decorator
    def glossaryPut(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}'
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def glossaryReadCategories(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/categories'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryReadCategoriesHeaders(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/categories/headers'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryReadDetailed(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/detailed'
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}

    @decorator
    def glossaryPutPartial(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/partial'
        self.payload = get_json(args, '--payloadFile')
        self.params = {'includeTermHierarchy': args['--includeTermHierarchy']}

    @decorator
    def glossaryReadTerms(self, args):
        glossaryName = 'Glossary'
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms' if args['--glossaryGuid'] else f'/api/glossary/name/{glossaryName}/terms'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort'], 'extInfo': args['--extInfo'], 'includeTermHierarchy': args['--includeTermHierarchy'], 'api-version': '2021-05-01-preview'}

    @decorator
    def glossaryReadTermsHeaders(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms/headers'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryCreateTermsExport(self, args):
        self.method = 'POST'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms/export'
        self.payload = args['--termGuid']
        self.params = {
            'api-version': '2021-05-01-preview',
            'includeTermHierarchy': args['--includeTermHierarchy']
            }

    @decorator
    def glossaryCreateTermsImport(self, args):
        glossaryName = 'Glossary'
        self.method = 'POST'
        self.endpoint = f'/api/glossary/{args["--glossaryGuid"]}/terms/import' if args['--glossaryGuid'] else f'/api/glossary/name/{glossaryName}/terms/import'
        self.files = {'file': open(args["--glossaryFile"], 'rb')}
        self.params = {
            "api-version": "2021-05-01-preview",
            'includeTermHierarchy': args['--includeTermHierarchy']
        }
        
    @decorator
    def glossaryReadTermsImport(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/glossary/terms/import/{args["--operationGuid"]}'
        self.params = {'api-version': '2021-05-01-preview'}


    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def glossaryCreateTemplate(self, args):
    #     self.method = 'POST'
    #     self.endpoint = '/api/atlas/v2/glossary/import'
    #     self.payload = get_json(args, '--payloadFile')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def glossaryReadTemplate(self, args):
    #     self.method = 'GET'
    #     self.endpoint = '/api/atlas/v2/glossary/import/template'