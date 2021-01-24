class PurviewGlossaryTerm():
    def __init__(self, name, glossaryGuid, **kwargs):
        self.name = name
        self.anchor = {'glossaryGuid': glossaryGuid}
        self.longDescription = kwargs.get('longDescription', None)
        self.status = kwargs.get('status', None)
        self.abbreviation = kwargs.get('abbreviation', None)
        self.contacts = {'Expert': kwargs.get('experts', []), 'Steward': kwargs.get('stewards', [])}
        self.resources = kwargs.get('resources', [])
        self.synonyms = kwargs.get('synonyms', [])
        self.seeAlso = kwargs.get('relatedTerms', [])
        self.attributes = kwargs.get('attributes', {})

class PurviewGlossary():
    def __init__(self, name, **kwargs):
        self.name = name

class PurviewGlossaryCategory():
    def __init__(self, name, glossaryGuid, **kwargs):
        self.name = name
        self.anchor = {'glossaryGuid': glossaryGuid}
