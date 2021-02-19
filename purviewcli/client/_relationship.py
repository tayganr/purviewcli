from .client import get_data
from purviewcli.model.atlas import AtlasRelationship

# ---------------------------
# RELATIONSHIP
# ---------------------------
def relationshipCreate(args):
    endpoint = '/api/atlas/v2/relationship'
    relationship = AtlasRelationship()
    relationship.typeName = args['--typeName']
    relationship.status = args.get('--status','ACTIVE')
    relationship.end1 = {
        'guid': args['--end1Guid'],
        'typeName': args['--end1Type']
    }
    relationship.end2 = {
        'guid': args['--end2Guid'],
        'typeName': args['--end2Type']
    }
    payload = relationship.__dict__
    del payload['guid']
    http_dict = {'app': 'catalog', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def relationshipRead(args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['--relationshipGuid']
    params = {'extendedInfo': args.get('--extendedInfo', False)}
    http_dict = {'app': 'catalog', 'method': 'GET', 'endpoint': endpoint, 'params': params, 'payload': None}
    data = get_data(http_dict)
    return data

def relationshipUpdate(args):
    endpoint = '/api/atlas/v2/relationship'
    relationship = relationshipRead({'--relationshipGuid': args['--relationshipGuid']})
    relationship = AtlasRelationship.from_json(relationship['relationship'])
    relationship.status = args.get('--status') if args.get('--status') else relationship.status
    payload = relationship.__dict__
    http_dict = {'app': 'catalog', 'method': 'PUT', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def relationshipDelete(args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['--relationshipGuid']
    http_dict = {'app': 'catalog', 'method': 'DELETE', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
    return data
