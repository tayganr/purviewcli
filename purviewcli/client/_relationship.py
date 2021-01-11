def getRelationshipGuid(self, args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['--guid'][0]
    params = {'extendedInfo': args['--extendedInfo']}
    data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    return data
