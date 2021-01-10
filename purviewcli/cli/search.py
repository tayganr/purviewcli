from purviewcli.common import http_get

def search(config, args):
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

    data = http_get('catalog', 'POST', endpoint, None, payload, config)
    return data
