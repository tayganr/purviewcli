import itertools
from .client import get_data
from purviewcli.model import AtlasEntity, AtlasEntityWithExtInfo, AtlasEntitiesWithExtInfo, AtlasClassification, ClassificationAssociateRequest

# ---------------------------
# ENTITY
# ---------------------------
def entityCreate(args):
  endpoint = '/api/atlas/v2/entity'
  # Entity
  entity = AtlasEntity()
  entity.attributes = {
    'name': args.get('--name')[0],
    'description': args.get('--description'),
    'qualifiedName': args.get('--qualifiedName')[0]
  }
  entity.typeName = args.get('--typeName')[0]
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
  params = {
    'ignoreRelationships': args.get('--ignoreRelationships', False),
    'minExtInfo': args.get('--minExtInfo', False)
  }
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityUpdate(args):
  endpoint = '/api/atlas/v2/entity/guid/%s' % args['--guid'][0]
  params = {'name': args['--attrKey']}
  payload = args['--attrVal']
  http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': params, 'payload': payload}
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

def entityReadHeader(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/header' % args['--guid'][0]
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

# ---------------------------
# BULK
# ---------------------------
def entityCreateBulk(args):
  endpoint = '/api/atlas/v2/entity/bulk'
  entities = AtlasEntitiesWithExtInfo()
  for name, qualifiedName, typeName in itertools.zip_longest(args['--name'], args['--qualifiedName'], args['--typeName']):
    entity = AtlasEntity()
    entity.attributes = {
      'name': name,
      'qualifiedName': qualifiedName
    }
    entity.typeName = typeName
    entity = entity.__dict__
    del entity['guid']
    entities.entities.append(entity)
  payload = entities.__dict__
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityReadBulk(args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {
    'ignoreRelationships': args.get('--ignoreRelationships', False),
    'minExtInfo': args.get('--minExtInfo', False),
    'guid': args['--guid']
  }
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityCreateBulkClassification(args):
  endpoint = '/api/atlas/v2/entity/bulk/classification'
  associate_request = ClassificationAssociateRequest()
  classification = AtlasClassification()
  classification.typeName = args['--classificationName'][0]
  associate_request.classification = classification.__dict__
  for guid in args['--guid']:
    associate_request.entityGuids.append(guid)
  payload = associate_request.__dict__
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data

# RequestInvalid
# pv entity deleteBulk --guid=<val>...
def entityDeleteBulk(args):
  endpoint = '/api/atlas/v2/entity/bulk'
  params = {'guid': args['--guid']}
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# RequestUriNotFound
# pv entity readBulkHeaders [--tagUpdateStartTime=<val>]
def entityReadBulkHeaders(args):
  endpoint = '/api/atlas/v2/entity/bulk/headers'
  params = None if args['--tagUpdateStartTime'] is None else {'tagUpdateStartTime': args['--tagUpdateStartTime']}
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# ---------------------------
# CLASSIFICATIONS
# ---------------------------
def entityCreateClassifications(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % (args['--guid'][0])
  payload = []
  for name in args.get('--classificationName'):
    classification = AtlasClassification()
    classification.typeName = name
    payload.append(classification.__dict__)
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityReadClassifications(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/classifications' % args['--guid'][0]
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

# ---------------------------
# CLASSIFICATION
# ---------------------------
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

# ---------------------------
# UNIQUE ATTRIBUTE (ENTITY)
# ---------------------------
def entityReadBulkUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/entity/bulk/uniqueAttribute/type/%s' % args['--typeName'][0]
  params = {'ignoreRelationships': args['--ignoreRelationships'], 'minExtInfo': args['--minExtInfo']}

  counter = 0
  for attrKey, attrVal in itertools.zip_longest(args['--attrKey'], args['--attrVal']):
    params['attr_' + str(counter) + ':' + attrKey] = attrVal
    counter += 1

  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityReadUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s' % args['--typeName'][0]
  params = {
    'ignoreRelationships': args['--ignoreRelationships'],
    'minExtInfo': args['--minExtInfo'],
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def entityUpdateUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s' % args['--typeName'][0]
  entity = entityReadUniqueAttributeType(args)
  entity = AtlasEntityWithExtInfo.from_json(entity)
  entity.entity['attributes']['description'] = args['--description']
  payload = entity.__dict__
  params = {
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': params, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityDeleteUniqueAttributeType(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s' % args['--typeName'][0]
  params = {
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# RequestUriNotFound
# pv entity readUniqueAttributeTypeHeader --typeName=<val> --attrKey=<val> --attrVal=<val>
def entityReadUniqueAttributeTypeHeader(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/header' % args['--typeName'][0]
  params = {
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# ---------------------------
# UNIQUE ATTRIBUTE (CLASSIFICATION)
# ---------------------------
def entityCreateUniqueAttributeTypeClassifications(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/classifications' % args['--typeName'][0]
  payload = []
  for name in args.get('--classificationName'):
    classification = AtlasClassification()
    classification.typeName = name
    payload.append(classification.__dict__)
  params = {
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': params, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityUpdateUniqueAttributeTypeClassifications(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/classifications' % args['--typeName'][0]
  entity = entityReadUniqueAttributeType(args)
  entity = AtlasEntityWithExtInfo.from_json(entity)

  payload = []
  for x in entity.entity['classifications']:
    if x['typeName'] in args.get('--classificationName'):
      classification = AtlasClassification.from_json(x)
      # Update classification here
      payload.append(classification.__dict__)

  params = {
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': params, 'payload': payload}
  data = get_data(http_dict)
  return data

def entityDeleteUniqueAttributeTypeClassification(args):
  endpoint = '/api/atlas/v2/entity/uniqueAttribute/type/%s/classification/%s' % (args['--typeName'][0], args['--classificationName'][0])
  params = {
    'attr:' + args['--attrKey'][0]: args['--attrVal'][0]
  }
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

# ---------------------------
# OTHER
# ---------------------------
# RequestUriNotFound
# pv entity readAudit --guid=<val> [--auditAction=<val> --count=<val> --startKey=<val>]
def entityReadAudit(args):
  endpoint = '/api/atlas/v2/entity/guid/%s/audit' % args['--guid'][0]
  params = {
    'auditAction': args.get('--auditAction'),
    'count': args.get('--count', 100),
    'startKey': args.get('--startKey')
  }
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data
