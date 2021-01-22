class PurviewClassificationDef():
    def __init__(self, name, **kwargs):
        self.category = 'CLASSIFICATION'
        self.description = kwargs.get('description')
        self.name = name
        self.options = {
            'displayName': kwargs.get('displayName')
        }
