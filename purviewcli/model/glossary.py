class PurviewGlossaryTerm():
    def __init__(self, attrs={}):
        self.name = attrs['--termName']
        self.longDescription = attrs['--termDescription']
        self.anchor = {'glossaryGuid': attrs['--glossaryGuid']}
        self.status = attrs['--termStatus']
        self.abbreviation = attrs['--termAcronym']
        self.contacts = {'Expert': [], 'Steward': []}
        self.resources = []
        self.synonyms = []
        self.seeAlso = []
        self.attributes = {}

        for expert in attrs['--expertId']:
            self.contacts['Expert'].append({'id': expert})
        for steward in attrs['--stewardId']:
            self.contacts['Steward'].append({'id': steward})
        for resourceName, resourceUrl in zip(attrs['--resourceName'],attrs['--resourceUrl']):
            self.resources.append({'displayName': resourceName, 'url': resourceUrl})
        for synonym in attrs['--synonym']:
            self.synonyms.append({'termGuid': synonym})
        for related in attrs['--related']:
            self.seeAlso.append({'termGuid': related})
