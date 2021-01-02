from purviewcli.common import http_get

# No data found
def getEntityAudit(config, args):
  endpoint = '/api/atlas/v2/entity/%s/audit' % args['--guid'][0]
  params = {'count': args['--count']}
  if args['--auditAction']:
    params['auditAction'] = args['--auditAction']
  if args['--startKey']:
    params['startKey'] = args['--startKey']
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data

def getEntityBulk(config, args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo'], 'guid': args['--guid']}
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data

# RequestUriNotFound
def getEntityBulkHeaders(config, args):
  endpoint = '/api/atlas/v2/entity/bulk/headers'
  params = None if args['--tagUpdateStartTime'] is None else {'tagUpdateStartTime': args['--tagUpdateStartTime']}
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data

# RequestUriNotFound
def getEntityBusinessmetadataImportTemplate(config, args):
  endpoint = '/api/atlas/v2/entity/businessmetadata/import/template'
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getEntityGuid(config, args):
  endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data

def getEntityGuidClassification(config, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classification/%s' % (args['--guid'][0], args['--classificationName'])
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getEntityGuidClassifications(config, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % args['--guid'][0]
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

def getEntityGuidHeader(config, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/header' % args['--guid'][0]
  data = http_get('catalog', 'GET', endpoint, None, None, config)
  return data

# No data found
def getEntityBulkUniqueAttributeType(config, args):
  endpoint = '/api/atlas/v2/entity/bulk/uniqueAttribute/type/%s' % args['--typeName']
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data

# No data found
def getEntityUniqueAttributeType(config, args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s' % args['--typeName']
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo'], 'attr:' + args['--attrKey']: args['--attrVal']}
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data

# No data/valid URI
def getEntityUniqueAttributeTypeHeader(config, args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/header' % args['--typeName']
  params = {'attr:' + args['--attrKey']: args['--attrVal']}
  data = http_get('catalog', 'GET', endpoint, params, None, config)
  return data
