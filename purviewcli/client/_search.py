from .client import get_data

# ---------------------------
# SEARCH
# ---------------------------
def searchQuery(args):
    endpoint = '/api/search/query'
    payload = {
        'keywords': args['--keywords'],
        'filter': args['--filter'],
        'limit': args['--limit'],
        'offset': args['--offset'],
        'facets': args['--facets']
    }

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data
