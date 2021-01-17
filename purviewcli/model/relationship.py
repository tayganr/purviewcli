class PurviewRelationship():
    def __init__(self, typeName, **kwargs):
        self.typeName = typeName
        self.end1 = {
            'guid': kwargs.get('end1Guid'),
            'typeName': kwargs.get('end1TypeName')
        }
        self.end2 = {
            'guid': kwargs.get('end2Guid'),
            'typeName': kwargs.get('end2TypeName')
        }
        self.status = kwargs.get('status')
