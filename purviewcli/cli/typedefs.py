from purviewcli.common import http_get

def getBusinessmetadatadef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Businessmetadatadef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getClassificationdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/classificationdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getEntitydef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/entitydef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getEnumdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/enumdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getRelationshipdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/relationshipdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getStructdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/structdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getTypedef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Typedef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getTypedefs(config, args):
  endpoint = '/api/atlas/v2/types/typedefs'
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getTypedefsHeaders(config, args):
  endpoint = '/api/atlas/v2/types/typedefs/headers'
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data
