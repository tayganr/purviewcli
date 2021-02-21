from .client import get_data
from purviewcli.model import AtlasEntity, AtlasEntityWithExtInfo
from purviewcli.model import PurviewEntity, PurviewClassification

# ---------------------------
# ENTITY
# ---------------------------
def entityCreate(args):
  endpoint = '/api/atlas/v2/entity'

  # Entity
  entity = AtlasEntity()
  entity.attributes = {
    'name': args.get('--name'),
    'description': args.get('--description'),
    'qualifiedName': args.get('--qualifiedName')
  }
  entity.typeName = args.get('--typeName')
  entity = entity.__dict__
  del entity['guid']

  # Payload
  payload = AtlasEntityWithExtInfo()
  payload.entity = entity
  payload = payload.__dict__
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityRead(args):
  endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityDelete(args):
  endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def entityReadAudit(args):
  endpoint = '/api/atlas/v2/entity/%s/audit' % args['--guid'][0]
  params = {'count': args['--count']}
  if args['--auditAction']:
    params['auditAction'] = args['--auditAction']
  if args['--startKey']:
    params['startKey'] = args['--startKey']
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityReadBulk(args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo'], 'guid': args['--guid']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# Request is not recognized. Please verify the HTTP method, header or URL
def entityDeleteBulk(args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {'guid': args['--guid']}
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# RequestUriNotFound
def entityReadBulkHeaders(args):
  endpoint = '/api/atlas/v2/entity/bulk/headers'
  params = None if args['--tagUpdateStartTime'] is None else {'tagUpdateStartTime': args['--tagUpdateStartTime']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# RequestUriNotFound
def entityReadBusinessmetadataImportTemplate(args):
  endpoint = '/api/atlas/v2/entity/businessmetadata/import/template'
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def entityCreateBulk(args):
  endpoint = '/api/atlas/v2/entity/bulk'
  payload = {'entities': []}
  for entityName, entityType, qualifiedName in zip(args.get('--entityName',[]), args.get('--entityType',[]), args.get('--qualifiedName',[])):
    entity = PurviewEntity(
      name = entityName,
      typeName = entityType,
      status = args.get('--status')[0] if len(args['--status'])>0 else 'ACTIVE',
      qualifiedName = qualifiedName
    )
    payload['entities'].append(entity.__dict__)
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityReadClassification(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classification/%s' % (args['--guid'][0], args['--classificationName'][0])
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def entityDeleteClassification(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classification/%s' % (args['--guid'][0], args['--classificationName'][0])
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def entityCreateClassifications(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % (args['--guid'][0])
  payload = []
  for item in args.get('--classificationName'):
    classification = PurviewClassification(typeName = item)
    payload.append(classification.__dict__)
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityReadClassifications(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % args['--guid'][0]
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def entityReadHeader(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/header' % args['--guid'][0]
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

# No data found
def entityReadBulkUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/entity/bulk/uniqueAttribute/type/%s' % args['--typeName']
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# No data found
def entityReadUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s' % args['--typeName']
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo'], 'attr:' + args['--attrKey']: args['--attrVal']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# No data/valid URI
def entityReadUniqueAttributeTypeHeader(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/header' % args['--typeName']
  params = {'attr:' + args['--attrKey']: args['--attrVal']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityCreateLabels(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/labels' % args['--guid'][0]
  payload = []
  for label in args['--label']:
      payload.append(label)
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data
