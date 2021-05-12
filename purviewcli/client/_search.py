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

    if args['--filter'] is not None:
        payload['filter'] = json.loads(args['--filter'])

    if args['--facets'] is not None:
        payload['facets'] = json.loads(args['--facets'])

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data
