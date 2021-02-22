from .client import get_data

# ---------------------------
# SEARCH
# ---------------------------
def searchAdvanced(args):
    endpoint = '/api/atlas/v2/search/advanced'
    payload = {
        'keywords': args['--keywords'],
        'limit': args['--limit'],
        'offset': args['--offset'],
        'facets': []
    }

    for facet in args['--facet']:
        payload['facets'].append(
            {
                'count': 0,
                'facet': facet,
                'sort': { 'count': 'desc'}
            }
        )

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data
