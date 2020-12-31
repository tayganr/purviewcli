from purviewcli.common import http_get

def getRelationshipGuid(config, args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['--guid'][0]
    params = {'extendedInfo': args['--extendedInfo']}
    data = http_get(endpoint, params, config)
    return data
