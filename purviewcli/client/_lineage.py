def lineageRead(args):
  endpoint = '/api/atlas/v2/lineage/%s' %  args['<guid>']
  params = {
    'depth': args['--depth'],
    'width': args['--width'],
    'direction': args['--direction'],
    'forceNewApi': args['--forceNewApi'],
    'includeParent': args['--includeParent'],
    'getDerivedLineage': args['--getDerivedLineage']
  }
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

# Request URI not found
def lineageReadUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/lineage/uniqueAttribute/type/%s' % args['--typeName']
  params = {'depth': args['--depth'], 'direction': args['--direction']}  
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data
