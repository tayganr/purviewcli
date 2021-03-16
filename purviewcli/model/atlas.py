class AtlasBaseModelObject():
    def __init__(self, **kwargs):
        self.guid = kwargs.get('guid')       

class AtlasStruct():
    def __init__(self, **kwargs):
        self.attributes = kwargs.get('attributes')
        self.typeName = kwargs.get('typeName')
        self.lastModifiedTS = kwargs.get('lastModifiedTS')
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
# ENTITY
# ---------------------------
class AtlasEntityExtInfo():
    def __init__(self, **kwargs):
        self.referredEntities = kwargs.get('referredEntities')

class AtlasEntityWithExtInfo(AtlasEntityExtInfo):
    def __init__(self, **kwargs):
        AtlasEntityExtInfo.__init__(self, **kwargs)
        self.entity = kwargs.get('entity')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasEntityWithExtInfo>'

class AtlasEntitiesWithExtInfo(AtlasEntityExtInfo):
    def __init__(self, **kwargs):
        AtlasEntityExtInfo.__init__(self, **kwargs)
        self.entities = []

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasEntityWithExtInfo>'

class AtlasEntity(AtlasStruct):
    def __init__(self, **kwargs):
        AtlasStruct.__init__(self, **kwargs)
        self.classifications = kwargs.get('classifications')
        self.createTime = kwargs.get('createTime')
        self.createdBy = kwargs.get('createdBy')
        self.guid = kwargs.get('guid')
        self.homeId = kwargs.get('homeId')
        self.meanings = kwargs.get('meanings')
        self.provenanceType = kwargs.get('provenanceType')
        self.proxy = kwargs.get('proxy')
        self.relationshipAttributes = kwargs.get('relationshipAttributes')
        self.status = kwargs.get('status')
        self.updateTime = kwargs.get('updateTime')
        self.updatedBy = kwargs.get('updatedBy')
        self.version = kwargs.get('version')
        self.source = kwargs.get('source')
        self.sourceDetails = kwargs.get('sourceDetails')
        self.contacts = kwargs.get('contacts')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasEntity { self.typeName }>'

# ---------------------------
# CLASSIFICATION
# ---------------------------
class AtlasClassification(AtlasStruct):
    def __init__(self, **kwargs):
        AtlasStruct.__init__(self, **kwargs)
        self.entityGuid = kwargs.get('entityGuid')
        self.entityStatus = kwargs.get('entityStatus')
        self.propagate = kwargs.get('propagate')
        self.removePropagationsOnEntityDelete = kwargs.get('removePropagationsOnEntityDelete')
        self.validityPeriods = kwargs.get('validityPeriods')
        self.source = kwargs.get('source')
        self.sourceDetails = kwargs.get('sourceDetails')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasClassification { self.typeName }>'

class ClassificationAssociateRequest():
    def __init__(self, **kwargs):
        self.classification = kwargs.get('classification')
        self.entityGuids = []

# ---------------------------
# RELATIONSHIP
# ---------------------------
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

# ---------------------------
# TYPES
# ---------------------------
class AtlasTypesDef():
    def __init__(self, **kwargs):
        self.classificationDefs = []
        self.entityDefs = []
        self.enumDefs = []
        self.relationshipDefs = []
        self.structDefs = []

class AtlasBaseTypeDef():
    def __init__(self, **kwargs):
        self.category = kwargs.get('category')
        self.createTime = kwargs.get('createTime')
        self.createdBy = kwargs.get('createdBy')
        self.dateFormatter = kwargs.get('dateFormatter')
        self.description = kwargs.get('description')
        self.guid = kwargs.get('guid')
        self.name = kwargs.get('name')
        self.options = kwargs.get('options')
        self.serviceType = kwargs.get('serviceType')
        self.typeVersion = kwargs.get('typeVersion')
        self.updateTime = kwargs.get('updateTime')
        self.updatedBy = kwargs.get('updatedBy')
        self.version = kwargs.get('version')
        self.lastModifiedTS = kwargs.get('lastModifiedTS')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasBaseTypeDef { self.name }>'

class AttributeDef():
    def __init__(self, **kwargs):
        self.cardinality = kwargs.get('cardinality')
        self.constraints = kwargs.get('constraints')
        self.defaultValue = kwargs.get('defaultValue')
        self.description = kwargs.get('description')
        self.includeInNotification = kwargs.get('includeInNotification')
        self.isIndexable = kwargs.get('isIndexable')
        self.isOptional = kwargs.get('isOptional')
        self.isUnique = kwargs.get('isUnique')
        self.name = kwargs.get('name')
        self.options = kwargs.get('options')
        self.typeName = kwargs.get('typeName')
        self.valuesMaxCount = kwargs.get('valuesMaxCount')
        self.valuesMinCount = kwargs.get('valuesMinCount')

class AtlasEnumDef(AtlasBaseTypeDef):
    def __init__(self, **kwargs):
        AtlasBaseTypeDef.__init__(self, **kwargs)
        self.defaultValue = kwargs.get('defaultValue')
        self.elementDefs = kwargs.get('elementDefs')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

class AtlasStructDef(AtlasBaseTypeDef):
    def __init__(self, **kwargs):
        AtlasBaseTypeDef.__init__(self, **kwargs)
        self.attributeDefs = kwargs.get('attributeDefs')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

class AtlasClassificationDef(AtlasStructDef):
    def __init__(self, **kwargs):
        AtlasStructDef.__init__(self, **kwargs)
        self.entityTypes = kwargs.get('entityTypes')
        self.subTypes = kwargs.get('subTypes')
        self.superTypes = kwargs.get('superTypes')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

class AtlasEntityDef(AtlasStructDef):
    def __init__(self, **kwargs):
        AtlasStructDef.__init__(self, **kwargs)
        self.subTypes = kwargs.get('subTypes')
        self.superTypes = kwargs.get('superTypes')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)

    def __repr__(self):
        return f'<AtlasEntityDef { self.name }>'

class AtlasRelationshipDef(AtlasStructDef):
    def __init__(self, **kwargs):
        AtlasStructDef.__init__(self, **kwargs)
        self.endDef1 = kwargs.get('endDef1')
        self.endDef2 = kwargs.get('endDef2')
        self.propagateTags = kwargs.get('propagateTags')
        self.relationshipCategory = kwargs.get('relationshipCategory')
        self.relationshipLabel = kwargs.get('relationshipLabel')

    @classmethod
    def from_json(cls, json_dict):
        return cls(**json_dict)