def getBusinessmetadatadef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Businessmetadatadef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getClassificationdef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/classificationdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getEntitydef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/entitydef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getEnumdef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/enumdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getRelationshipdef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/relationshipdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getStructdef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/structdef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getTypedef(self, args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'][0] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/Typedef/%s/%s' % (typeDefKey,typeDefVal)
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getTypedefs(self, args):
  endpoint = '/api/atlas/v2/types/typedefs'
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getTypedefsHeaders(self, args):
  endpoint = '/api/atlas/v2/types/typedefs/headers'
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data
