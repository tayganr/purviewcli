import itertools
from purviewcli.model import PurviewGlossaryTerm, PurviewGlossary, PurviewGlossaryCategory

def getGlossary(self, args):
    glossaryGuid = '' if args['--glossaryGuid'] is None else args['--glossaryGuid']
    endpoint = '/api/atlas/v2/glossary/%s' % glossaryGuid
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def createGlossary(self, args):
    endpoint = '/api/atlas/v2/glossary'
    glossary = PurviewGlossary(name=args['--name'])
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=glossary.__dict__)
    return data

def createGlossaryCategory(self, args):
    endpoint = '/api/atlas/v2/glossary/category'
    glossaryGuid = getGlossaryGuid(self, args)
    category = PurviewGlossaryCategory(
        name=args['--categoryName'][0],
        glossaryGuid=glossaryGuid
        )
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=category.__dict__)
    return data

def createGlossaryCategories(self, args):
    endpoint = '/api/atlas/v2/glossary/categories'
    glossaryGuid = getGlossaryGuid(self, args)
    payload = []
    for categoryName in args['--categoryName']:
        category = PurviewGlossaryCategory(
            name=categoryName,
            glossaryGuid=glossaryGuid
        )
        payload.append(category.__dict__)
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

# RequestUriNotFound
def assignEntities(self, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    payload = []
    for guid in args['--guid']:
        payload.append({'guid': guid})
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getAssignedEntities(self, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def deleteAssignedEntities(self, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    assignedEntities = getAssignedEntities(self, {
        '--termGuid': args['--termGuid'],
        '--limit': -1,
        '--offset': 0,
        '--sort': 'ASC'
    })
    payload = []
    for entity in assignedEntities:
        if entity['guid'] in args['--guid']:
            payload.append({
                'guid': entity['guid'],
                'relationshipGuid': entity['relationshipGuid']
            })
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=payload)
    return data

# RequestUriNotFound
def getGlossaryTemplate(self, args):
    endpoint = '/api/atlas/v2/glossary/import/template'
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getGlossaryCategories(self, args):
    endpoint = '/api/atlas/v2/glossary/%s/categories' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def getGlossaryCategoriesHeaders(self, args):
    endpoint = '/api/atlas/v2/glossary/%s/categories/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def getGlossaryCategory(self, args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getGlossaryCategoryRelated(self, args):
    endpoint = '/api/atlas/v2/glossary/category/%s/related' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def getGlossaryCategoryTerms(self, args):
    endpoint = '/api/atlas/v2/glossary/category/%s/terms' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def getGlossaryDetailed(self, args):
    endpoint = '/api/atlas/v2/glossary/%s/detailed' % args['--glossaryGuid']
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getGlossaryTerms(self, args):
    endpoint = '/api/atlas/v2/glossary/%s/terms' % args['--glossaryGuid']
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getGlossaryTermsHeaders(self, args):
    endpoint = '/api/atlas/v2/glossary/%s/terms/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def getGlossaryTermsRelated(self, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/related' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data

def getGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def createGlossaryTerms(self, args):
    endpoint = '/api/atlas/v2/glossary/terms'
    glossaryGuid = getGlossaryGuid(self, args)
    payload = []
    for termName, termDescription, termStatus in itertools.zip_longest(args['--termName'], args['--longDescription'], args['--status']):
        glossaryTerm = PurviewGlossaryTerm(
            name = termName,
            glossaryGuid = glossaryGuid,
            longDescription = termDescription,
            status = termStatus
        )
        payload.append(glossaryTerm.__dict__)

    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def createGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term'
    glossaryGuid = getGlossaryGuid(self, args)
    glossaryTerm = PurviewGlossaryTerm(
        name = args.get('--termName')[0],
        glossaryGuid = glossaryGuid,
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

    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=glossaryTerm.__dict__)
    return data

def updateGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    term = getGlossaryTerm(self, {'--termGuid': args['--termGuid']})

    term['longDescription'] = args.get('--longDescription') if args.get('--longDescription') else term.get('longDescription')
    term['status'] = args.get('--status') if args.get('--status') else term.get('status')
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

    term['synonyms'] = [] if args.get('--synonym') else term['synonyms']
    for synonym in args.get('--synonym', []):
        term['synonyms'].append({'termGuid': synonym})

    term['seeAlso'] = [] if args.get('--related') else term['seeAlso']
    for related in args.get('--related'):
        term['seeAlso'].append({'termGuid': related})

    data = self.http_get(app='catalog', method='PUT', endpoint=endpoint, params=None, payload=term)
    return data    

def deleteGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data

def purgeGlossaryTerms(self, args):
    glossaryGuid = None
    print('[INFO] Retrieving glossary GUID.')
    if not args['--glossaryGuid']:
        glossary = getGlossary(self, args)[0]
        glossaryGuid = glossary['guid']
    else:
        glossaryGuid = args['--glossaryGuid']  
    
    print('[INFO] Retrieving glossary details.')
    glossary_detail = getGlossaryDetailed(self, {
        '--glossaryGuid': glossaryGuid
    })

    print('[INFO] Glossary with GUID: %s and Name: %s has %s terms.' % (
        glossary_detail['guid'],
        glossary_detail['name'],
        len(glossary_detail['terms']) if 'terms' in glossary_detail else '0'
    ))
    if 'termInfo' in glossary_detail: 
        for termGuid in glossary_detail['termInfo']:
            if 'assignedEntities' in glossary_detail['termInfo'][termGuid]:
                print('[INFO] Term is assigned to Entities.')
                endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % termGuid
                payload = glossary_detail['termInfo'][termGuid]['assignedEntities']
                data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=payload)
                print(data)
            print(deleteGlossaryTerm(self, {'--termGuid': termGuid}))

    data = {'msg':'purgeGlossaryTerms complete.'}
    return data

def deleteGlossary(self, args):
    endpoint = '/api/atlas/v2/glossary/%s' % args['--glossaryGuid']
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data

def deleteGlossaryCategory(self, args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data

def getGlossaryGuid(self, args):
    glossaryGuid = None
    if not args['--glossaryGuid']:
        glossary = getGlossary(self, args)
        glossaryGuid = glossary[0]['guid']
    else:
        glossaryGuid = args['--glossaryGuid']
    return glossaryGuid
