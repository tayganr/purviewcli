import sys
import itertools
from .client import get_data
from purviewcli.model.atlas import AtlasTypesDef, AtlasBaseTypeDef, AttributeDef, AtlasEntityDef

# ---------------------------
# TYPEDEFS
# ---------------------------
def typesCreateTypedefs(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  typedefs = AtlasTypesDef()

  for category, name, description in itertools.zip_longest(args['--category'], args['--defName'], args['--defDescription']):
    typedef = AtlasBaseTypeDef()
    typedef.category = category
    typedef.name = name
    typedef.description = description
    item = typedef.__dict__
    del item['guid']

    if category == 'CLASSIFICATION':
      typedefs.classificationDefs.append(item)
    elif category == 'ENTITY':
      typedefs.entityDefs.append(item)
    elif category == 'ENUM':
      typedefs.entityDefs.append(item)
    elif category == 'RELATIONSHIP':
      typedefs.entityDefs.append(item)
    elif category == 'STRUCT':
      typedefs.structDefs.append(item)
    else:
        print("[ERROR] Category '%s' is invalid. Valid categories include: CLASSIFICATION, ENTITY, ENUM, RELATIONSHIP, or STRUCT." % category)
        sys.exit()

  payload = typedefs.__dict__
  http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
  data = get_data(http_dict)
  return data

def typesReadTypedefs(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  params = {'type': args['--type']} if args['--type'] else None
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
  data = get_data(http_dict)
  return data

def typesUpdateTypedefs(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  typedefs = AtlasTypesDef()

  for category, name, description in itertools.zip_longest(args['--category'], args['--defName'], args['--defDescription']):
    typedef = typesReadTypedef({'--guid': None, '--name': name})
    typedef = AtlasBaseTypeDef.from_json(typedef)
    typedef.category = category
    typedef.description = description

    item = typedef.__dict__
    if category == 'CLASSIFICATION':
      typedefs.classificationDefs.append(item)
    elif category == 'ENTITY':
      typedefs.entityDefs.append(item)
    elif category == 'ENUM':
      typedefs.entityDefs.append(item)
    elif category == 'RELATIONSHIP':
      typedefs.entityDefs.append(item)
    elif category == 'STRUCT':
      typedefs.structDefs.append(item)
    else:
        print("[ERROR] Category '%s' is invalid. Valid categories include: CLASSIFICATION, ENTITY, ENUM, RELATIONSHIP, or STRUCT." % category)
        sys.exit()

  payload = typedefs.__dict__
  http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
  data = get_data(http_dict)
  return data

def typesAddAttributedef(args):
  # Attribute Definition
  attr = AttributeDef()
  attr.cardinality = "SINGLE"
  attr.includeInNotification = False
  attr.isIndexable = False
  attr.isOptional = True
  attr.isUnique = False
  attr.name = args['--name']
  attr.typeName = args['--type']
  attr.valuesMaxCount = 1
  attr.valuesMinCount = 0

  # Entity Definition
  typedef = typesReadTypedef({'--guid': None, '--name': args['--typeName']})
  typedef = AtlasEntityDef.from_json(typedef)
  typedef.attributeDefs.append(attr.__dict__)

  # Types Definition
  item = typedef.__dict__
  typedefs = AtlasTypesDef()
  typedefs.entityDefs.append(item)
  payload = typedefs.__dict__

  # Request
  endpoint = '/api/atlas/v2/types/typedefs'
  http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
  data = get_data(http_dict)
  return data

def typesDeleteTypedefs(args):
  endpoint = '/api/atlas/v2/types/typedefs'
  typedefs = AtlasTypesDef()

  for name in args['--defName']:
    typedef = typesReadTypedef({'--guid': None, '--name': name})
    typedef = AtlasBaseTypeDef.from_json(typedef)
    category = typedef.category
    item = typedef.__dict__
    if category == 'CLASSIFICATION':
      typedefs.classificationDefs.append(item)
    elif category == 'ENTITY':
      typedefs.entityDefs.append(item)
    elif category == 'ENUM':
      typedefs.entityDefs.append(item)
    elif category == 'RELATIONSHIP':
      typedefs.entityDefs.append(item)
    elif category == 'STRUCT':
      typedefs.structDefs.append(item)
    else:
        print("[ERROR] Category '%s' is invalid. Valid categories include: CLASSIFICATION, ENTITY, ENUM, RELATIONSHIP, or STRUCT." % category)
        sys.exit()

  payload = typedefs.__dict__
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':payload}
  data = get_data(http_dict)
  return data

def typesReadTypedefsHeaders(args):
  endpoint = '/api/atlas/v2/types/typedefs/headers'
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesReadTypedef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/typedef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesDeleteTypedefName(args):
  endpoint = '/api/atlas/v2/types/typedef/name/%s' % args['--name']
  http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesReadBusinessmetadatadef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/businessmetadatadef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesReadClassificationdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/classificationdef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data
  
def typesReadEntitydef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/entitydef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesReadEnumdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/enumdef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesReadRelationshipdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/relationshipdef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data

def typesReadStructdef(args):
  typeDefKey = 'guid' if args['--name'] is None else 'name'
  typeDefVal = args['--guid'] if args['--name'] is None else args['--name']
  endpoint = '/api/atlas/v2/types/structdef/%s/%s' % (typeDefKey,typeDefVal)
  http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
  data = get_data(http_dict)
  return data
