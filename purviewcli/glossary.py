import json
from purviewcli.common import http_get

def getGlossary(config, args):
    glossaryGuid = '' if args['--glossaryGuid'] is None else args['--glossaryGuid']
    endpoint = '/api/atlas/v2/glossary/%s' % glossaryGuid
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryCategories(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/categories' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryCategoriesHeaders(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/categories/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryCategory(config, args):
    endpoint = '/api/atlas/v2/glossary/category/%s' % args['--categoryGuid']
    data = http_get('catalog', 'GET', endpoint, None, None, config)
    return data

def getGlossaryCategoryRelated(config, args):
    endpoint = '/api/atlas/v2/glossary/category/%s/related' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryCategoryTerms(config, args):
    endpoint = '/api/atlas/v2/glossary/category/%s/terms' % args['--categoryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryDetailed(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/detailed' % args['--glossaryGuid']
    data = http_get('catalog', 'GET', endpoint, None, None, config)
    return data

def getGlossaryTerm(config, args):
    endpoint = '/api/atlas/v2/glossary/term/%s' % args['--termGuid']
    data = http_get('catalog', 'GET', endpoint, None, None, config)
    return data

def getGlossaryTerms(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/terms' % args['--glossaryGuid']
    data = http_get('catalog', 'GET', endpoint, None, None, config)
    return data

def getGlossaryTermsAssignedEntities(config, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/assignedEntities' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryTermsHeaders(config, args):
    endpoint = '/api/atlas/v2/glossary/%s/terms/headers' % args['--glossaryGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def getGlossaryTermsRelated(config, args):
    endpoint = '/api/atlas/v2/glossary/terms/%s/related' % args['--termGuid']
    params = {'limit': args['--limit'], 'offset': args['--offset'], 'sort': args['--sort']}
    data = http_get('catalog', 'GET', endpoint, params, None, config)
    return data

def newGlossaryTerm(config, args):
    glossary = getGlossary(config, args)
    glossary_guid = json.loads(glossary)[0]['guid']
    endpoint = '/api/atlas/v2/glossary/term'
    payload = {
        "name": args['--termName'],
        "anchor":{"glossaryGuid": glossary_guid},
        "status": args['--termStatus'],
        "longDescription": args['--termDescription'],
        "abbreviation": args['--termAcronym'],
        "synonyms":[],
        "seeAlso":[],
        "attributes":{}
    }
    for termGuid in args['--synonym']:
        payload['synonyms'].append({'termGuid': termGuid})

    for termGuid in args['--related']:
        payload['seeAlso'].append({'termGuid': termGuid})

    data = http_get('catalog', 'POST', endpoint, None, payload, config)
    return data



# {
#     "name":"Another Term",
#     "anchor":{"glossaryGuid":"505674a3-d8fc-4234-9038-e313829a7216"},
#     "status":"Alert",
#     "longDescription":"This is the term definition.",
#     "abbreviation":"acro1, acro2, acro3",
#     "resources":[{"displayName":"resource1","url":"https://google.com"}],
#     "synonyms":[{"termGuid":"a6bf5214-91d8-4c04-bdfc-d171bfee6eaa"},{"termGuid":"f87e4915-470a-43ac-a801-db245aa65212"}],
#     "seeAlso":[{"termGuid":"6cbfe86d-bbac-4823-a9df-d354528c99ad"}],
#     "contacts":{"Expert":[{"id":"095354ff-cae8-44ff-8120-22ec5a941b40","info":"Information here."}],"Steward":[{"id":"095354ff-cae8-44ff-8120-22ec5a941b40","info":"More information."}]},
#     "attributes":{"New Term Template":{"Employee ID":"1234"}}}