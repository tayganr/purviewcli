from .endpoint import Endpoint, decorator, get_json

class Glossary(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def glossaryRead(self, args):
        self.method = 'GET'
        self.endpoint = '/api/atlas/v2/glossary' if args["--glossaryGuid"] is None else f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryCreate(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryCreateCategories(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/categories'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryCreateCategory(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/category'
        self.payload = get_json(args, '--payload-file')

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
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryPutCategoryPartial(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/category/{args["--categoryGuid"]}/partial'
        self.payload = get_json(args, '--payload-file')

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
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryDeleteTerm(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}'

    @decorator
    def glossaryReadTerm(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}'

    @decorator
    def glossaryPutTerm(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryPutTermPartial(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/term/{args["--termGuid"][0]}/partial'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryCreateTerms(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/glossary/terms'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryDeleteTermsAssignedEntities(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryReadTermsAssignedEntities(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryCreateTermsAssignedEntities(self, args):
        self.method = 'POST'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryPutTermsAssignedEntities(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/terms/{args["--termGuid"][0]}/assignedEntities'
        self.payload = get_json(args, '--payload-file')

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
        self.payload = get_json(args, '--payload-file')

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

    @decorator
    def glossaryPutPartial(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/partial'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def glossaryReadTerms(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    @decorator
    def glossaryReadTermsHeaders(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms/headers'
        self.params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}

    # 
    @decorator
    def glossaryCreateTermsExport(self, args):
        self.method = 'POST'
        self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms/export'
        self.payload = args['--termGuid']        

    @decorator
    def glossaryCreateTermsImport(self, args):
        self.method = 'POST'
        if args["--glossaryName"] is None:
            self.endpoint = f'/api/atlas/v2/glossary/{args["--glossaryGuid"]}/terms/import'
        else:
            self.endpoint = f'/api/atlas/v2/glossary/name/{args["--glossaryName"]}/terms/import'

    @decorator
    def glossaryReadTerms(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/name/{args["--glossaryName"]}/terms'

    @decorator
    def glossaryReadTermsImport(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/glossary/terms/import/{args["--operationGuid"]}'

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def glossaryCreateTemplate(self, args):
    #     self.method = 'POST'
    #     self.endpoint = '/api/atlas/v2/glossary/import'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def glossaryReadTemplate(self, args):
    #     self.method = 'GET'
    #     self.endpoint = '/api/atlas/v2/glossary/import/template'