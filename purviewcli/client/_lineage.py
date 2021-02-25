from .client import get_data

# ---------------------------
# LINEAGE
# ---------------------------
def lineageRead(args):
  endpoint = '/api/atlas/v2/lineage/%s' %  args['--guid']
  params = {
    'depth': args.get('--depth', 3),
    'width': args.get('--width', 6),
    'direction': args.get('--direction', 'BOTH'),
    'forceNewApi': 'true',
    'includeParent': 'true',
    'getDerivedLineage': 'false'
  }
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# Request URI not found
def lineageReadUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/lineage/uniqueAttribute/type/%s' % args['--typeName']
  params = {
    'depth': args.get('--depth', 3),
    'direction': args.get('--direction', 'BOTH'),
    'attr:' + args['--attrKey']: args['--attrVal']
  }  
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data
