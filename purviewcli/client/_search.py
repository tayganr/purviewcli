from .endpoint import Endpoint, decorator, get_json

class Search(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def searchQuery(self, args):
        self.method = 'POST'
        self.endpoint = '/api/search/query'
        self.payload = {
            'keywords': args['--keywords'],
            'limit': args['--limit'],
            'offset': args['--offset'],
            'filter': get_json(args,'--filter-file'),
            'facets': get_json(args,'--facets-file')
        }
