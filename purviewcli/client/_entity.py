# No data found
from purviewcli.model import PurviewEntity, PurviewClassification

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

# Request is not recognized. Please verify the HTTP method, header or URL
def deleteEntityBulk(self, args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {'guid': args['--guid']}
  data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=params, payload=None)
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

def getEntity(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
  return data

def deleteEntity(self, args):
    endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data

def createEntity(self, args):
    endpoint = '/api/atlas/v2/entity'
    entity = PurviewEntity(
      name = args.get('--entityName')[0],
      typeName = args.get('--entityType')[0],
      status = 'ACTIVE' if args.get('--status') is None else args.get('--status'),
      description = args.get('--description'),
      qualifiedName = args.get('--qualifiedName')[0]
    )
    payload = {
      'entity': entity.__dict__
    }
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def createEntityBulk(self, args):
    endpoint = '/api/atlas/v2/entity/bulk'
    payload = {'entities': []}
    for entityName, entityType, qualifiedName in zip(args.get('--entityName',[]), args.get('--entityType',[]), args.get('--qualifiedName',[])):
      entity = PurviewEntity(
        name = entityName,
        typeName = entityType,
        status = 'ACTIVE' if args.get('--status') is None else args.get('--status'),
        qualifiedName = qualifiedName
      )
      payload['entities'].append(entity.__dict__)
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getEntityClassification(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classification/%s' % (args['--guid'][0], args['--classificationName'][0])
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def deleteEntityClassification(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classification/%s' % (args['--guid'][0], args['--classificationName'][0])
  data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
  return data

def addEntityClassifications(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % (args['--guid'][0])
  payload = []
  for item in args.get('--classificationName'):
    classification = PurviewClassification(typeName = item)
    payload.append(classification.__dict__)
  data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
  return data

def getEntityClassifications(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % args['--guid'][0]
  data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
  return data

def getEntityHeader(self, args):
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

def assignLabels(self, args):
  endpoint = '/api/atlas/v2/entity/guid/%s/labels' % args['--guid'][0]
  payload = []
  for label in args['--label']:
      payload.append(label)
  data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
  return data
