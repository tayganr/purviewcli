from purviewcli.common import http_get

def search(config, args):
    endpoint = '/api/atlas/v2/search/advanced'
    payload = {
        'keywords': args['--keywords'],
        'limit': args['--limit'],
        'offset': args['--offset']
    }
    data = http_get('catalog', 'POST', endpoint, None, payload, config)
    return data
