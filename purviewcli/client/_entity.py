# No data found
def getEntityAudit(self, args):
  endpoint = '/api/atlas/v2/entity/%s/audit' % args['--guid'][0]
  params = {'count': args['--count']}
  if args['--auditAction']:
    params['auditAction'] = args['--auditAction']
  if args['--startKey']:
    params['startKey'] = args['--startKey']
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

def getEntityBulk(self, args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo'], 'guid': args['--guid']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

# RequestUriNotFound
def getEntityBulkHeaders(self, args):
  endpoint = '/api/atlas/v2/entity/bulk/headers'
  params = None if args['--tagUpdateStartTime'] is None else {'tagUpdateStartTime': args['--tagUpdateStartTime']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

# RequestUriNotFound
def getEntityBusinessmetadataImportTemplate(self, args):
  endpoint = '/api/atlas/v2/entity/businessmetadata/import/template'
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getEntityGuid(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

def getEntityGuidClassification(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classification/%s' % (args['--guid'][0], args['--classificationName'])
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getEntityGuidClassifications(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % args['--guid'][0]
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getEntityGuidHeader(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/header' % args['--guid'][0]
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

# No data found
def getEntityBulkUniqueAttributeType(self, args):
  endpoint = '/api/atlas/v2/entity/bulk/uniqueAttribute/type/%s' % args['--typeName']
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

# No data found
def getEntityUniqueAttributeType(self, args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s' % args['--typeName']
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo'], 'attr:' + args['--attrKey']: args['--attrVal']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

# No data/valid URI
def getEntityUniqueAttributeTypeHeader(self, args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/header' % args['--typeName']
  params = {'attr:' + args['--attrKey']: args['--attrVal']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data
