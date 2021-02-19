class AtlasBaseModelObject():
    def __init__(self, **kwargs):
        self.guid = kwargs.get('guid')       

# ---------------------------
# GLOSSARY
# ---------------------------
class AtlasGlossaryBaseObject(AtlasBaseModelObject):
    def __init__(self, **kwargs):
        AtlasBaseModelObject.__init__(self, **kwargs)
        self.longDescription = kwargs.get('longDescription')
        self.name = kwargs.get('name')
        self.qualifiedName = kwargs.get('qualifiedName')
        self.shortDescription = kwargs.get('shortDescription')
        self.classifications = kwargs.get('classifications')

class AtlasGlossaryCategory(AtlasGlossaryBaseObject):
    def __init__(self, **kwargs):
        AtlasGlossaryBaseObject.__init__(self, **kwargs)
        self.anchor = kwargs.get('anchor')
        self.childrenCategories = kwargs.get('childrenCategories')
        self.parentCategory = kwargs.get('parentCategory')
        self.terms = kwargs.get('terms')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasGlossaryCategory { self.name }>'

class AtlasGlossary(AtlasGlossaryBaseObject):
    def __init__(self, **kwargs):
        AtlasGlossaryBaseObject.__init__(self, **kwargs)
        self.categories = kwargs.get('categories')
        self.language = kwargs.get('language')
        self.terms = kwargs.get('terms')
        self.usage = kwargs.get('usage')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasGlossary { self.name }>'

class AtlasGlossaryTerm(AtlasGlossaryBaseObject):
    def __init__(self, **kwargs):
        AtlasGlossaryBaseObject.__init__(self, **kwargs)
        self.abbreviation = kwargs.get('abbreviation')
        self.anchor = kwargs.get('anchor')
        self.antonyms = kwargs.get('antonyms')
        self.createTime = kwargs.get('createTime')
        self.createdBy = kwargs.get('createdBy')
        self.updateTime = kwargs.get('updateTime')
        self.updatedBy = kwargs.get('updatedBy')
        self.status = kwargs.get('status')
        self.resources = kwargs.get('resources')
        self.contacts = kwargs.get('contacts')
        self.attributes = kwargs.get('attributes')
        self.assignedEntities = kwargs.get('assignedEntities')
        self.categories = kwargs.get('categories')
        self.classifies = kwargs.get('classifies')
        self.examples = kwargs.get('examples')
        self.isA = kwargs.get('isA')
        self.preferredTerms = kwargs.get('preferredTerms')
        self.preferredToTerms = kwargs.get('preferredToTerms')
        self.replacedBy = kwargs.get('replacedBy')
        self.replacementTerms = kwargs.get('replacementTerms')
        self.seeAlso = kwargs.get('seeAlso')
        self.synonyms = kwargs.get('synonyms')
        self.translatedTerms = kwargs.get('translatedTerms')
        self.translationTerms = kwargs.get('translationTerms')
        self.usage = kwargs.get('usage')
        self.validValues = kwargs.get('validValues')
        self.validValuesFor = kwargs.get('validValuesFor')
    
    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasGlossaryTerm { self.name }>'


class AtlasObjectId():
    def __init__(self, **kwargs):
        self.guid = kwargs.get('guid')
        self.typeName = kwargs.get('typeName')
        self.uniqueAttributes = kwargs.get('uniqueAttributes')

class AtlasRelatedObjectId(AtlasObjectId):
    def __init__(self, **kwargs):
        AtlasObjectId.__init__(self, **kwargs)
        self.displayText = kwargs.get('displayText')
        self.entityStatus = kwargs.get('entityStatus')
        self.relationshipAttributes = kwargs.get('relationshipAttributes')
        self.relationshipGuid = kwargs.get('relationshipGuid')
        self.relationshipStatus = kwargs.get('relationshipStatus')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasRelatedObjectId { self.displayText }>'

# ---------------------------
# RELATIONSHIP
# ---------------------------
class AtlasStruct():
    def __init__(self, **kwargs):
        self.attributes = kwargs.get('attributes')
        self.typeName = kwargs.get('typeName')
        self.lastModifiedTS = kwargs.get('lastModifiedTS')

# AtlasRelationship
class AtlasRelationship(AtlasStruct):
    def __init__(self, **kwargs):
        AtlasStruct.__init__(self, **kwargs)
        self.blockedPropagatedClassifications = kwargs.get('blockedPropagatedClassifications')
        self.createTime = kwargs.get('createTime')
        self.createdBy = kwargs.get('createdBy')
        self.end1 = kwargs.get('end1')
        self.end2 = kwargs.get('end2')
        self.guid = kwargs.get('guid')
        self.homeId = kwargs.get('homeId')
        self.label = kwargs.get('label')
        self.propagateTags = kwargs.get('propagateTags')
        self.propagatedClassifications = kwargs.get('propagatedClassifications')
        self.provenanceType = kwargs.get('provenanceType')
        self.status = kwargs.get('status')
        self.updateTime = kwargs.get('updateTime')
        self.updatedBy = kwargs.get('updatedBy')
        self.version = kwargs.get('version')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasRelationship { self.typeName }>'

# Apache Atlas Python Client
# https://github.com/apache/atlas/tree/d99ea4b3fb6dad2c076f073d5b64b2ac5748f70a/intg/src/main/python
