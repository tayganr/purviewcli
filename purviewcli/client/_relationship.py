from purviewcli.model import PurviewRelationship
from purviewcli.client import _entity as entity

def relationshipRead(args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['<guid>']
    params = {'extendedInfo': args['--extendedInfo']}
    return {
        'app': 'catalog',
        'method': 'GET',
        'endpoint': endpoint,
        'params': params,
        'payload': None
    }
    # data = self.http_get(app='catalog', method='GET', endpoint=endpoint, params=params, payload=None)
    # return data

def relationshipDelete(args):
    endpoint = '/api/atlas/v2/relationship/guid/%s' % args['<guid>']
    data = self.http_get(app='catalog', method='DELETE', endpoint=endpoint, params=None, payload=None)
    return data

def relationshipCreate(args):
    endpoint = '/api/atlas/v2/relationship'
    end1 = entity.getEntity(
        self,
        {
            '<guid>':[args.get('--end1Guid')],
            '--ignoreRelationships': False,
            '--minExtInfo': False
        }
    )
    end2 = entity.getEntity(
        self,
        {
            '<guid>':[args.get('--end2Guid')],
            '--ignoreRelationships': False,
            '--minExtInfo': False
        }
    )
    relationship = PurviewRelationship(
        typeName = args.get('--typeName'),
        end1Guid = args.get('--end1Guid'),
        end1TypeName = end1['entity']['typeName'],
        end2Guid = args.get('--end2Guid'),
        end2TypeName = end2['entity']['typeName'],
        status = args.get('--status')[0] if len(args['--status'])>0 else 'ACTIVE'
    )
    data = self.http_get(app='catalog', method='POST', endpoint=endpoint, params=None, payload=relationship.__dict__)
    return data

def relationshipUpdate(args):
    # endpoint = '/api/atlas/v2/relationship'
    # relationship = getRelationship(
    #     self,
    #     {
    #         '<guid>': args['<guid>'],
    #         '--extendedInfo': False
    #     }
    # )['relationship']
    # data = self.http_get(app='catalog', method='PUT', endpoint=endpoint, params=None, payload=relationship)
    data = {}
    return data
  