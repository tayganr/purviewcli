import itertools
from .client import get_data
from purviewcli.model import AtlasGlossary, AtlasGlossaryTerm, AtlasGlossaryCategory, AtlasRelatedObjectId

# ---------------------------
# GLOSSARY
# ---------------------------
def glossaryCreate(args):
    endpoint = '/api/atlas/v2/glossary'
    glossary = AtlasGlossary()
    glossary.name = args['--glossaryName']
    payload = glossary.__dict__
    del payload['guid']
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data
    
def glossaryRead(args):
    glossaryGuid = args['--glossaryGuid'] if args['--glossaryGuid'] else ''
    endpoint = '/api/atlas/v2/glossary/%s' % glossaryGuid
    params = {
        'limit': args.get('--limit',-1),
        'offset': args.get('--offset',0),
        'sort': args.get('--sort','ASC')
    }
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryUpdate(args):
    endpoint = '/api/atlas/v2/glossary/%s' % args['--glossaryGuid']
    glossary = glossaryRead({'--glossaryGuid': args['--glossaryGuid']})
    glossary = AtlasGlossary.from_json(glossary)
    glossary.language = args['--language']
    payload = glossary.__dict__
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryDelete(args):
    endpoint = '/api/atlas/v2/glossary/%s' % args['--glossaryGuid']
    http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryReadDetailed(args):
    endpoint = '/api/atlas/v2/glossary/%s/detailed' % args['--glossaryGuid']
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryUpdatePartial(args):
    endpoint = endpoint = '/api/atlas/v2/glossary/%s/partial' % args['--glossaryGuid']
    payload = {}
    for attrKey, attrVal in itertools.zip_longest(args['--attrKey'], args['--attrVal']):
        payload[attrKey] = attrVal
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

# ---------------------------
# TERMS
# ---------------------------
def glossaryCreateTerm(args):
    endpoint = '/api/atlas/v2/glossary/term'
    glossaryTerm = AtlasGlossaryTerm()

    # General
    glossaryTerm.anchor = {'glossaryGuid': args['--glossaryGuid']}
    glossaryTerm.name = args.get('--termName')[0]
    glossaryTerm.longDescription = args.get('--longDescription')[0] if len(args['--longDescription'])>0 else None
    glossaryTerm.status = args.get('--status')[0] if len(args['--status'])>0 else None
    glossaryTerm.abbreviation = args.get('--abbreviation')

    # Contacts
    glossaryTerm.contacts = {'Expert': [], 'Steward': []}
    for expert in args.get('--expertId'):
        glossaryTerm.contacts['Expert'].append({'id': expert})
    for steward in args.get('--stewardId'):
        glossaryTerm.contacts['Steward'].append({'id': steward})

    # Resources
    glossaryTerm.resources = []
    for resourceName, resourceUrl in zip(args.get('--resourceName',[]),args.get('--resourceUrl',[])):
        glossaryTerm.resources.append({'displayName': resourceName, 'url': resourceUrl})

    # Synonyms
    glossaryTerm.synonyms = []
    for synonym in args.get('--synonym'):
        glossaryTerm.synonyms.append({'termGuid': synonym})

    # Related
    glossaryTerm.seeAlso = []
    for related in args.get('--related'):
        glossaryTerm.seeAlso.append({'termGuid': related})

    # Delete GUID
    payload = glossaryTerm.__dict__
    del payload['guid']

    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryReadTerm(args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryUpdateTerm(args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    term = glossaryReadTerm({'--termGuid': args['--termGuid']})
    term = AtlasGlossaryTerm.from_json(term)

    # General
    term.longDescription = args.get('--longDescription')[0] if args.get('--longDescription') else term.longDescription
    term.status = args.get('--status')[0] if args.get('--status') else term.status
    term.abbreviation = args.get('--abbreviation') if args.get('--abbreviation') else term.abbreviation

    # Contacts
    for expert in args.get('--expertId', []):
        term.contacts['Expert'].append({'id': expert})
    for steward in args.get('--stewardId', []):
        term.contacts['Steward'].append({'id': steward})

    # Resources
    for resourceName, resourceUrl in zip(args.get('--resourceName',[]),args.get('--resourceUrl',[])):
        term.resources.append({'displayName': resourceName, 'url': resourceUrl})

    # Synonyms
    for synonym in args.get('--synonym', []):
        term.synonyms.append({'termGuid': synonym})

    # Related
    for related in args.get('--related'):
        term.seeAlso.append({'termGuid': related})
    
    payload = term.__dict__
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryDeleteTerm(args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryUpdateTermPartial(args):
    endpoint = '/api/atlas/v2/glossary/term/%s/partial' % args['--termGuid']
    payload = {}
    for attrKey, attrVal in itertools.zip_longest(args['--attrKey'], args['--attrVal']):
        payload[attrKey] = attrVal
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryCreateTerms(args):
    endpoint = '/api/atlas/v2/glossary/terms'
    payload = []
    for termName, termDescription, termStatus in itertools.zip_longest(args['--termName'], args['--longDescription'], args['--status']):
        glossaryTerm = AtlasGlossaryTerm()
        glossaryTerm.anchor = {'glossaryGuid': args['--glossaryGuid']}
        glossaryTerm.name = termName
        glossaryTerm.longDescription = termDescription
        glossaryTerm.status = termStatus
        item = glossaryTerm.__dict__
        del item['guid']
        payload.append(item)
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryReadTerms(args):
    endpoint = '/api/atlas/v2/glossary/%s/terms' % args['--glossaryGuid']
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryReadTermsHeaders(args):
    endpoint = '/api/atlas/v2/glossary/%s/terms/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryReadTermsRelated(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/related' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

# ---------------------------
# ASSIGNED ENTITIES
# ---------------------------
def glossaryCreateAssignedEntities(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    payload = []
    for guid in args['--guid']:
        relatedObject = AtlasRelatedObjectId()
        relatedObject.guid = guid
        payload.append(relatedObject.__dict__)
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryReadAssignedEntities(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryDeleteAssignedEntities(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    payload = []
    for guid, relationshipGuid in zip(args['--guid'], args['--relationshipGuid']):
        payload.append({'guid': guid, 'relationshipGuid': relationshipGuid})
    http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

# ---------------------------
# CATEGORY
# ---------------------------
def glossaryCreateCategory(args):
    endpoint = '/api/atlas/v2/glossary/category'
    category = AtlasGlossaryCategory()
    category.name = args['--categoryName'][0]
    category.anchor = {'glossaryGuid': args['--glossaryGuid']}
    payload = category.__dict__
    del payload['guid']
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryReadCategory(args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryUpdateCategory(args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    category = glossaryReadCategory({'--categoryGuid': args['--categoryGuid']})
    category = AtlasGlossaryCategory.from_json(category)
    category.longDescription = args.get('--longDescription')[0] if args.get('--longDescription') else category.longDescription
    payload = category.__dict__
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryDeleteCategory(args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryUpdateCategoryPartial(args):
    endpoint = '/api/atlas/v2/glossary/category/%s/partial' % args['--categoryGuid']
    payload = {}
    for attrKey, attrVal in itertools.zip_longest(args['--attrKey'], args['--attrVal']):
        payload[attrKey] = attrVal
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryReadCategoryRelated(args):
    endpoint = '/api/atlas/v2/glossary/category/%s/related' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryReadCategoryTerms(args):
    endpoint = '/api/atlas/v2/glossary/category/%s/terms' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryCreateCategories(args):
    endpoint = '/api/atlas/v2/glossary/categories'
    glossaryGuid = args['--glossaryGuid']
    payload = []
    for categoryName in args['--categoryName']:
        category = AtlasGlossaryCategory()
        category.name = categoryName
        category.anchor = {'glossaryGuid': args['--glossaryGuid']}
        item = category.__dict__
        del item['guid']
        payload.append(item)
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}
    data = get_data(http_dict)
    return data

def glossaryReadCategories(args):
    endpoint = '/api/atlas/v2/glossary/%s/categories' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data

def glossaryReadCategoriesHeaders(args):
    endpoint = '/api/atlas/v2/glossary/%s/categories/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    data = get_data(http_dict)
    return data
    
# ---------------------------
# TEMPLATE
# ---------------------------
# RequestUriNotFound
# pv glossary readTemplate
def glossaryReadTemplate(args):
    endpoint = '/api/atlas/v2/glossary/import/template'
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data

# RequestInvalid
# pv glossary uploadTemplate
def glossaryUploadTemplate(args):
    endpoint = '/api/atlas/v2/glossary/import'
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':None}
    data = get_data(http_dict)
    return data