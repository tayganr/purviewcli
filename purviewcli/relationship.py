from purviewcli.common import http_get_catalog

def getRelationshipGuid(config, args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['--guid'][0]
    params = {'extendedInfo': args['--extendedInfo']}
    data = http_get_catalog(endpoint, params, config)
    return data
