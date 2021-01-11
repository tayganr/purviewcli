def search(self, args):
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

    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data
