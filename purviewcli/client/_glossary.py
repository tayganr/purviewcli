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

def getGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def newGlossaryTerm(self, args):
    if not args['--glossaryGuid']:
        glossary = getGlossary(self, args)
        args['--glossaryGuid'] = glossary[0]['guid']
    endpoint = '/api/atlas/v2/glossary/term'
    glossaryTerm = PurviewGlossaryTerm(args)
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=glossaryTerm.__dict__)
    return data

def delGlossaryTerm(self, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data
