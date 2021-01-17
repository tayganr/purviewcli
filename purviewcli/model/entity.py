class PurviewEntity():
    def __init__(self, name, typeName, qualifiedName, **kwargs):
        self.typeName = typeName
        self.status = kwargs.get('status')
        self.attributes = {
            'name': name,
            'description': kwargs.get('description'),
            'qualifiedName': qualifiedName
        }
