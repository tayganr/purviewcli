from .endpoint import Endpoint, decorator, get_json

class Entity(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'catalog'

    @decorator
    def entityCreate(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/entity'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityDeleteBulk(self, args):
        self.method = 'DELETE'
        self.endpoint = '/api/atlas/v2/entity/bulk'
        self.params = {'guid': args['--guid']}

    @decorator
    def entityReadBulk(self, args):
        self.method = 'GET'
        self.endpoint = '/api/atlas/v2/entity/bulk'
        self.params = {'guid': args['--guid'], 'ignoreRelationships': str(args['--ignoreRelationships']).lower(), 'minExtInfo': str(args['--minExtInfo']).lower()}

    @decorator
    def entityCreateBulk(self, args):
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/entity/bulk'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityCreateBulkClassification(self, args):
        # Associates a classification to multiple entities in bulk.
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/entity/bulk/classification'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityCreateBulkSetClassifications(self, args):
        # Set classifications on entities in bulk (Classification -< Entities).
        self.method = 'POST'
        self.endpoint = '/api/atlas/v2/entity/bulk/setClassifications'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityDelete(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}'

    @decorator
    def entityRead(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}'
        self.params = {'ignoreRelationships': str(args['--ignoreRelationships']).lower(), 'minExtInfo': str(args['--minExtInfo']).lower()}

    @decorator
    def entityPut(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}'
        self.params = {'name': args['--name']}
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityDeleteClassification(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/classification/{args["--classificationName"]}'

    @decorator
    def entityReadClassification(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/classification/{args["--classificationName"]}'

    @decorator
    def entityReadClassifications(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/classifications'

    @decorator
    def entityCreateClassifications(self, args):
        self.method = 'POST'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/classifications'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityPutClassifications(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/classifications'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityReadHeader(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/header'

    @decorator
    def entityReadBulkUniqueAttribute(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/entity/bulk/uniqueAttribute/type/{args["--typeName"]}'
        self.params = {'ignoreRelationships': str(args['--ignoreRelationships']).lower(), 'minExtInfo': str(args['--minExtInfo']).lower()}

    @decorator
    def entityReadUniqueAttribute(self, args):
        self.method = 'GET'
        self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}'
        self.params = {'attr:qualifiedName': args['--qualifiedName'], 'ignoreRelationships': str(args['--ignoreRelationships']).lower(), 'minExtInfo': str(args['--minExtInfo']).lower()}

    @decorator
    def entityDeleteUniqueAttribute(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}'

    @decorator
    def entityPutUniqueAttribute(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityDeleteUniqueAttributeClassification(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/classification/{args["--classificationName"]}'

    @decorator
    def entityCreateUniqueAttributeClassifications(self, args):
        self.method = 'POST'
        self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/classifications'
        self.payload = get_json(args, '--payload-file')

    @decorator
    def entityPutUniqueAttributeClassifications(self, args):
        self.method = 'PUT'
        self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/classifications'
        self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityCreateBusinessMetadataTemplate(self, args):
    #     self.method = 'POST'
    #     self.endpoint = '/api/atlas/v2/entity/businessmetadata/import'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityReadBusinessMetadataTemplate(self, args):
    #     self.method = 'GET'
    #     self.endpoint = '/api/atlas/v2/entity/businessmetadata/import/template'

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityDeleteBusinessMetadata(self, args):
    #     self.method = 'DELETE'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/businessmetadata'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityCreateBusinessMetadata(self, args):
    #     self.method = 'POST'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/businessmetadata'
    #     self.params = {'isOverwrite': str(args['--isOverwrite']).lower()}
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityDeleteBusinessMetadataName(self, args):
    #     self.method = 'DELETE'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/businessmetadata/{args["--bmName"]}'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityCreateBusinessMetadataName(self, args):
    #     self.method = 'POST'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/businessmetadata/{args["--bmName"]}'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityReadAudit(self, args):
    #     self.method = 'GET'
    #     self.endpoint = f'/api/atlas/v2/entity/{args["--guid"][0]}/audit'
    #     self.params = {'auditAction': args['--auditAction'], 'count': args['--count'], 'startKey': args['--startKey']}

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityReadTypeHeader(self, args):
    #     self.method = 'GET'
    #     self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/header'
    #     self.params = {'attr:qualifiedName': args['--qualifiedName']}

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityReadBulkHeaders(self, args):
    #     self.method = 'GET'
    #     self.endpoint = '/api/atlas/v2/entity/bulk/headers'
    #     self.params = {'tagUpdateStartTime': args['--tagUpdateStartTime']}

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityDeleteLabels(self, args):
    #     self.method = 'DELETE'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/labels'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityCreateLabels(self, args):
    #     self.method = 'POST'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/labels'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityPutLabels(self, args):
    #     self.method = 'PUT'
    #     self.endpoint = f'/api/atlas/v2/entity/guid/{args["--guid"][0]}/labels'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityDeleteTypeLabels(self, args):
    #     self.method = 'DELETE'
    #     self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/labels'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityCreateTypeLabels(self, args):
    #     self.method = 'POST'
    #     self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/labels'
    #     self.payload = get_json(args, '--payload-file')

    # NOT SUPPORTED IN AZURE PURVIEW
    # @decorator
    # def entityPutTypeLabels(self, args):
    #     self.method = 'PUT'
    #     self.endpoint = f'/api/atlas/v2/entity/uniqueAttribute/type/{args["--typeName"]}/labels'
    #     self.payload = get_json(args, '--payload-file')