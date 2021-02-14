import itertools
from purviewcli.model import PurviewGlossaryTerm, PurviewGlossary, PurviewGlossaryCategory

# ---------------------------
# GLOSSARY
# ---------------------------
def glossaryCreate(args):
    endpoint = '/api/atlas/v2/glossary'
    glossary = PurviewGlossary(name=args['--glossaryName'])
    return {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':glossary.__dict__}
    
def glossaryRead(args):
    glossaryGuid = args['--glossaryGuid'] if args['--glossaryGuid'] else ''
    endpoint = '/api/atlas/v2/glossary/%s' % glossaryGuid
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    
def glossaryDelete(args):
    endpoint = '/api/atlas/v2/glossary/%s' % args['--glossaryGuid']
    return {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':None}

def glossaryReadDetailed(args):
    endpoint = '/api/atlas/v2/glossary/%s/detailed' % args['--glossaryGuid']
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    
# ---------------------------
# TERMS
# ---------------------------
def glossaryCreateTerm(args):
    endpoint = '/api/atlas/v2/glossary/term'
    glossaryTerm = PurviewGlossaryTerm(
        name = args.get('--termName')[0],
        glossaryGuid = args['--glossaryGuid'],
        longDescription = args.get('--longDescription')[0] if len(args['--longDescription'])>0 else None,
        status = args.get('--status')[0] if len(args['--status'])>0 else None,
        abbreviation = args.get('--abbreviation'),
    )

    for expert in args.get('--expertId'):
        glossaryTerm.experts.append({'id': expert})

    for steward in args.get('--stewardId'):
        glossaryTerm.stewards.append({'id': steward})

    for resourceName, resourceUrl in zip(args.get('--resourceName',[]),args.get('--resourceUrl',[])):
        glossaryTerm.resources.append({'displayName': resourceName, 'url': resourceUrl})

    for synonym in args.get('--synonym'):
        glossaryTerm.synonyms.append({'termGuid': synonym})

    for related in args.get('--related'):
        glossaryTerm.relatedTerms.append({'termGuid': related})

    return {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':glossaryTerm.__dict__}

def glossaryReadTerm(args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
    
def glossaryUpdateTerm(args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    term = getGlossaryTerm({'--termGuid': args['--termGuid']})

    term['longDescription'] = args.get('--longDescription')[0] if args.get('--longDescription') else term.get('longDescription')
    term['status'] = args.get('--status')[0] if args.get('--status') else term.get('status')
    term['abbreviation'] = args.get('--abbreviation') if args.get('--abbreviation') else term.get('abbreviation')

    term['contacts']['Expert'] = [] if args.get('--expertId') else term['contacts']['Expert']
    for expert in args.get('--expertId', []):
        term['contacts']['Expert'].append({'id': expert})

    term['contacts']['Steward'] = [] if args.get('--stewardId') else term['contacts']['Steward']
    for steward in args.get('--stewardId', []):
        term['contacts']['Steward'].append({'id': steward})

    term['resources'] = [] if len(list(zip(args.get('--resourceName',[]),args.get('--resourceUrl',[])))) > 0 else term.get('resources')
    for resourceName, resourceUrl in zip(args.get('--resourceName',[]),args.get('--resourceUrl',[])):
        term['resources'].append({'displayName': resourceName, 'url': resourceUrl})

    term['synonyms'] = [] if args.get('--synonym') else term.get('synonyms')
    for synonym in args.get('--synonym', []):
        term['synonyms'].append({'termGuid': synonym})

    term['seeAlso'] = [] if args.get('--related') else term.get('seeAlso')
    for related in args.get('--related'):
        term['seeAlso'].append({'termGuid': related})

    print(term)
    return {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload':term}

def glossaryDeleteTerm(args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    return {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':None}

def glossaryCreateTerms(args):
    endpoint = '/api/atlas/v2/glossary/terms'
    glossaryGuid = args['--glossaryGuid']
    payload = []
    for termName, termDescription, termStatus in itertools.zip_longest(args['--termName'], args['--longDescription'], args['--status']):
        glossaryTerm = PurviewGlossaryTerm(
            name = termName,
            glossaryGuid = glossaryGuid,
            longDescription = termDescription,
            status = termStatus
        )
        payload.append(glossaryTerm.__dict__)
    return {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}

def glossaryReadTerms(args):
    endpoint = '/api/atlas/v2/glossary/%s/terms' % args['--glossaryGuid']
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}

def glossaryReadTermsHeaders(args):
    endpoint = '/api/atlas/v2/glossary/%s/terms/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}

def glossaryReadTermsRelated(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/related' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}

def glossaryCreateAssignedEntities(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    payload = []
    for guid in args['--guid']:
        payload.append({'guid': guid})
    return {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}

def glossaryReadAssignedEntities(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}

def glossaryDeleteAssignedEntities(args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    payload = []
    for guid, relationshipGuid in zip(args['--guid'], args['--relationshipGuid']):
        payload.append({'guid': guid, 'relationshipGuid': relationshipGuid})
    return {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':payload}

# ---------------------------
# CATEGORY
# ---------------------------
def glossaryCreateCategory(args):
    endpoint = '/api/atlas/v2/glossary/category'
    glossaryGuid = args['--glossaryGuid']
    category = PurviewGlossaryCategory(
        name=args['--categoryName'][0],
        glossaryGuid=glossaryGuid
        )
    return {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':category.__dict__}

def glossaryReadCategory(args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}

def glossaryDeleteCategory(args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    return {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload':None}

def glossaryReadCategoryRelated(args):
    endpoint = '/api/atlas/v2/glossary/category/%s/related' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}

def glossaryReadCategoryTerms(args):
    endpoint = '/api/atlas/v2/glossary/category/%s/terms' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}

def glossaryCreateCategories(args):
    endpoint = '/api/atlas/v2/glossary/categories'
    glossaryGuid = args['--glossaryGuid']
    payload = []
    for categoryName in args['--categoryName']:
        category = PurviewGlossaryCategory(
            name=categoryName,
            glossaryGuid=glossaryGuid
        )
        payload.append(category.__dict__)
    return {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload':payload}

def glossaryReadCategories(args):
    endpoint = '/api/atlas/v2/glossary/%s/categories' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}

def glossaryReadCategoriesHeaders(args):
    endpoint = '/api/atlas/v2/glossary/%s/categories/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload':None}
    
# ---------------------------
# TEMPLATE
# ---------------------------
# RequestUriNotFound
def glossaryReadTemplate(args):
    endpoint = '/api/atlas/v2/glossary/import/template'
    return {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload':None}
