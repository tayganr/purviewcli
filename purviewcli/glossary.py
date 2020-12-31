from purviewcli.common import http_get_catalog

def getGlossary(config, args):
    glossaryGuid = '' if args['--glossaryGuid'] is None else args['--glossaryGuid']
    endpoint = '/api/atlas/v2/glossary/%s' % glossaryGuid
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryCategories(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/categories' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryCategoriesHeaders(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/categories/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryCategory(config, args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    data = http_get_catalog(endpoint, None, config)
    return data

def getGlossaryCategoryRelated(config, args):
    endpoint = '/api/atlas/v2/glossary/category/%s/related' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryCategoryTerms(config, args):
    endpoint = '/api/atlas/v2/glossary/category/%s/terms' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryDetailed(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/detailed' % args['--glossaryGuid']
    data = http_get_catalog(endpoint, None, config)
    return data

def getGlossaryTerm(config, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = http_get_catalog(endpoint, None, config)
    return data

def getGlossaryTerms(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/terms' % args['--glossaryGuid']
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryTermsAssignedEntities(config, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryTermsHeaders(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/terms/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data

def getGlossaryTermsRelated(config, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/related' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get_catalog(endpoint, params, config)
    return data
