from .client import get_data
import json
import sys

# ---------------------------
# SEARCH
# ---------------------------
def getJSON(args, param):
    response = None
    if args[param] is not None:
        filepath = args[param]
        if '.JSON' in filepath.upper():
            with open(filepath) as json_file:
                response = json.load(json_file)
        else:
            print('[ERROR] The {0} parameter must contain a valid file path to a JSON document.'.format(param))
            sys.exit()
    return response

def searchQuery(args):
    endpoint = '/api/search/query'

    payload = {
        'keywords': args['--keywords'],
        'limit': args['--limit'],
        'offset': args['--offset']
    }
    payload['filter'] = getJSON(args,'--filter-file')
    payload['facets'] = getJSON(args,'--facets-file')

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data
