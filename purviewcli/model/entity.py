class PurviewEntity():
    def __init__(self, name, typeName, qualifiedName, **kwargs):
        self.typeName = typeName
        self.status = kwargs.get('status')
        self.source = kwargs.get('source')
        self.attributes = {
            'name': name,
            'displayName': kwargs.get('displayName'),
            'description': kwargs.get('description'),
            'qualifiedName': qualifiedName
        }
