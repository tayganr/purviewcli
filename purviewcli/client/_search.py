from .endpoint import Endpoint, decorator, get_json

class Search(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def searchQuery(self, args):
        self.method = 'POST'
        self.endpoint = '/api/search/query'
        self.params = {"api-version": "2021-05-01-preview"}
        self.payload = {
            'keywords': args['--keywords'],
            'limit': args['--limit'],
            'offset': args['--offset'],
            'filter': get_json(args,'--filterFile'),
            'facets': get_json(args,'--facets-file')
        }
    
    @decorator
    def searchAutoComplete(self, args):
        self.method = 'POST'
        self.endpoint = '/api/search/autocomplete'
        self.params = {"api-version": "2021-05-01-preview"}
        self.payload = {
            "keywords": args['--keywords'],
            "filter": get_json(args,'--filterFile'),
            "limit": args['--limit']
        }

    @decorator
    def searchSuggest(self, args):
        self.method = 'POST'
        self.endpoint = '/api/search/suggest'
        self.params = {"api-version": "2021-05-01-preview"}
        self.payload = {
            "keywords": args['--keywords'],
            "filter": get_json(args,'--filterFile'),
            "limit": args['--limit']
        }
    
    @decorator
    def searchBrowse(self, args):
        self.method = 'POST'
        self.endpoint = '/api/browse'
        self.params = {"api-version": "2021-05-01-preview"}
        self.payload = {
            "entityType": args['--entityType'],
            "path": args['--path'],
            "limit": args['--limit'],
            'offset': args['--offset']

        }
