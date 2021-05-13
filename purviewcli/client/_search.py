from .client import get_data
import json
import sys

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

    if args['--filter-file'] is not None:
        filepath = args['--filter-file']
        if '.JSON' in filepath.upper():
            with open(filepath) as json_file:
                payload['filter'] = json.load(json_file)
        else:
            print('[ERROR] The filter-file parameter must contain a valid file path to a JSON document.')
            sys.exit()

    if args['--facets-file'] is not None:
        filepath = args['--facets-file']
        if '.JSON' in filepath.upper():
            with open(filepath) as json_file:
                payload['facets'] = json.load(json_file)
        else:
            print('[ERROR] The facets-file parameter must contain a valid file path to a JSON document.')
            sys.exit()

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data
