from purviewcli.model import PurviewGlossaryTerm

def getGlossary(self, args):
    glossaryGuid = '' if args['--glossaryGuid'] is None else args['--glossaryGuid']
    endpoint = '/api/atlas/v2/glossary/%s' % glossaryGuid
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
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

def getGlossaryTermsAssignedEntities(self, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
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

# READ
def getGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

# CREATE
def createGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term'
    
    glossaryGuid = None
    if not args['--glossaryGuid']:
        glossary = getGlossary(self, args)
        glossaryGuid = glossary[0]['guid']

    glossaryTerm = PurviewGlossaryTerm(
        name = args.get('--termName'),
        glossaryGuid = glossaryGuid,
        longDescription = args.get('--longDescription'),
        status = args.get('--status'),
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

# UPDATE
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

# DELETE
def deleteGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data