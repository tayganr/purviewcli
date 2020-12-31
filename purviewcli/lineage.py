from purviewcli.common import http_get_catalog

def getLineage(config, args):
  endpoint = '/api/atlas/v2/lineage/%s' %  args['--guid'][0]
  params = {
    'depth': args['--depth'],
    'width': args['--width'],
    'direction': args['--direction'],
    'forceNewApi': args['--forceNewApi'],
    'includeParent': args['--includeParent'],
    'getDerivedLineage': args['--getDerivedLineage']
  }
  data = http_get_catalog(endpoint, params, config)
  return data

# Request URI not found
def getLineageUniqueAttributeType(config, args):
  endpoint = '/api/atlas/v2/lineage/uniqueAttribute/type/%s' % args['--typeName']
  params = {'depth': args['--depth'], 'direction': args['--direction']}  
  data = http_get_catalog(endpoint, params, config)
  return data
