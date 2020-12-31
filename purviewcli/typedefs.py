from purviewcli.common import http_get_catalog

def getTypesBusinessmetadatadef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Businessmetadatadef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesClassificationdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/classificationdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesEntitydef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/entitydef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesEnumdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/enumdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesRelationshipdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/relationshipdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesStructdef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/structdef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesTypedef(config, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Typedef/%s/%s' % (typeDefKey,typeDefVal)
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesTypedefs(config, args):
  endpoint = '/api/atlas/v2/types/typedefs'
  data = http_get_catalog(endpoint, None, config)
  return data

def getTypesTypedefsHeaders(config, args):
  endpoint = '/api/atlas/v2/types/typedefs/headers'
  data = http_get_catalog(endpoint, None, config)
  return data
