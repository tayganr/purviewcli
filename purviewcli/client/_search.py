from .client import get_data
import json

# ---------------------------
# SEARCH
# ---------------------------
def searchQuery(args):
    endpoint = '/api/search/query'

    payload = {
        'keywords': args['--keywords'],
        'limit': args['--limit'],
        'offset': args['--offset']
    }
    if '--filter' in args:
        payload['filter'] = json.loads(args['--filter'])
    if '--facets' in args:
        payload['facets'] = json.loads(args['--facets'])

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data
