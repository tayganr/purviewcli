
"""purviewcli

Usage:
  purviewcli config
  purviewcli [csv | json] getEntityAudit (--guid=<guid>) [--auditAction=<auditAction> --count=<count> --startKey=<startKey>]
  purviewcli [csv | json] getEntityBulk (--guid=<guid>...) [--ignoreRelationships --minExtInfo]
  purviewcli [csv | json] getEntityBulkHeaders [--tagUpdateStartTime=<tagUpdateStartTime>]
  purviewcli [csv | json] getEntityBulkUniqueAttributeType (--typeName=<typeName>) [--ignoreRelationships --minExtInfo]
  purviewcli [csv | json] getEntityBusinessmetadataImportTemplate
  purviewcli [csv | json] getEntityGuid (--guid=<guid>) [--ignoreRelationships --minExtInfo]
  purviewcli [csv | json] getEntityGuidClassification (--guid=<guid> --classificationName=<classificationName>)
  purviewcli [csv | json] getEntityGuidClassifications (--guid=<guid>)
  purviewcli [csv | json] getEntityGuidHeader (--guid=<guid>)
  purviewcli [csv | json] getEntityUniqueAttributeType (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>) [--ignoreRelationships --minExtInfo]
  purviewcli [csv | json] getEntityUniqueAttributeTypeHeader (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>)
  purviewcli [csv | json] getGlossary [--glossaryGuid=<glossaryGuid>] [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryCategories (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryCategoriesHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryCategory (--categoryGuid=<categoryGuid>)
  purviewcli [csv | json] getGlossaryCategoryRelated (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryCategoryTerms (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryDetailed (--glossaryGuid=<glossaryGuid>)
  purviewcli [csv | json] getGlossaryTerm (--termGuid=<termGuid>)
  purviewcli [csv | json] getGlossaryTerms (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryTermsAssignedEntities (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryTermsHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryTermsRelated (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getLineage (--guid=<guid>) [--depth=<depth> --width=<width> --direction=<direction> --forceNewApi --includeParent --getDerivedLineage]
  purviewcli [csv | json] getLineageUniqueAttributeType (--typeName=<typeName>) [--depth=<depth> --direction=<direction>]
  purviewcli [csv | json] getRelationshipGuid (--guid=<guid>) [--extendedInfo]
  purviewcli [csv | json] getTypesBusinessmetadatadef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesClassificationdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesEntitydef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesEnumdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesRelationshipdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesStructdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesTypedef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypesTypedefs
  purviewcli [csv | json] getTypesTypedefsHeaders

Options:
  -h --help                                   Show this screen.
  -v --version                                Show version.
  --limit=<limit>                             Page size, by default there is no paging [default: -1].
  --offset=<offset>                           Offset for pagination purpose [default: 0].
  --sort=<sort>                               ASC or DESC [default: ASC].
  --auditAction=<auditAction>                 BUSINESS_ATTRIBUTE_UPDATE or CLASSIFICATION_ADD or CLASSIFICATION_DELETE or CLASSIFICATION_UPDATE or ENTITY_CREATE or ENTITY_DELETE or ENTITY_IMPORT_CREATE or ENTITY_IMPORT_DELETE or ENTITY_IMPORT_UPDATE or ENTITY_PURGE or ENTITY_UPDATE or LABEL_ADD or LABEL_DELETE or PROPAGATED_CLASSIFICATION_ADD or PROPAGATED_CLASSIFICATION_DELETE or PROPAGATED_CLASSIFICATION_UPDATE or TERM_ADD or TERM_DELETE.
  --count=<count>                             Number of events required	[default: 100].
  --startKey=<startKey>                       Used for pagination. Startkey is inclusive, the returned results contain the event with the given startkey.
  --tagUpdateStartTime=<tagUpdateStartTime>   DataType long.
  --depth=<depth>                             Number of hops for lineage [default: 3].
  --width=<width>                             Custom to Azure Purview [default: 6].
  --direction=<direction>                     Offset for pagination purpose [default: BOTH].

"""
from docopt import docopt
from purviewcli import __version__
import purviewcli.common as common
import purviewcli.glossary as glossary
import purviewcli.entity as entity
import purviewcli.lineage as lineage
import purviewcli.relationship as relationship
import purviewcli.typedefs as typedefs

def main():
  # Initialise Arguments (docopt)
  args = docopt(__doc__, version=__version__)
  
  # Special Argument: config
  if args['config']:
    common.init_config()
  else:
    purview_api(args)

def purview_api(args):
  # Function Map
  function_map = {
    'getEntityAudit': entity.getEntityAudit,
    'getEntityBulk': entity.getEntityBulk,
    'getEntityBulkHeaders': entity.getEntityBulkHeaders,
    'getEntityBulkUniqueAttributeType': entity.getEntityBulkUniqueAttributeType,
    'getEntityBusinessmetadataImportTemplate': entity.getEntityBusinessmetadataImportTemplate,
    'getEntityGuid': entity.getEntityGuid,
    'getEntityGuidClassification': entity.getEntityGuidClassification,
    'getEntityGuidClassifications': entity.getEntityGuidClassifications,
    'getEntityGuidHeader': entity.getEntityGuidHeader,
    'getEntityUniqueAttributeType': entity.getEntityUniqueAttributeType,
    'getEntityUniqueAttributeTypeHeader': entity.getEntityUniqueAttributeTypeHeader,
    'getGlossary': glossary.getGlossary,
    'getGlossaryCategories': glossary.getGlossaryCategories,
    'getGlossaryCategoriesHeaders': glossary.getGlossaryCategoriesHeaders,
    'getGlossaryCategory': glossary.getGlossaryCategory,
    'getGlossaryCategoryRelated': glossary.getGlossaryCategoryRelated,
    'getGlossaryCategoryTerms': glossary.getGlossaryCategoryTerms,
    'getGlossaryDetailed': glossary.getGlossaryDetailed,
    'getGlossaryTerm': glossary.getGlossaryTerm,
    'getGlossaryTerms': glossary.getGlossaryTerms,
    'getGlossaryTermsAssignedEntities': glossary.getGlossaryTermsAssignedEntities,
    'getGlossaryTermsHeaders': glossary.getGlossaryTermsHeaders,
    'getGlossaryTermsRelated': glossary.getGlossaryTermsRelated,
    'getLineage': lineage.getLineage,
    'getLineageUniqueAttributeType': lineage.getLineageUniqueAttributeType,
    'getRelationshipGuid': relationship.getRelationshipGuid,
    'getTypesBusinessmetadatadef': typedefs.getTypesBusinessmetadatadef,
    'getTypesClassificationdef': typedefs.getTypesClassificationdef,
    'getTypesEntitydef': typedefs.getTypesEntitydef,
    'getTypesEnumdef': typedefs.getTypesEnumdef,
    'getTypesRelationshipdef': typedefs.getTypesRelationshipdef,
    'getTypesStructdef': typedefs.getTypesStructdef,
    'getTypesTypedef': typedefs.getTypesTypedef,
    'getTypesTypedefs': typedefs.getTypesTypedefs,
    'getTypesTypedefsHeaders': typedefs.getTypesTypedefsHeaders
  }

  config = common.read_config()
  command = common.selected_arg(args, function_map.keys())
  func = function_map[command]
  data = func(config, args)
  fileformat = common.selected_arg(args, ['csv','json'])
  common.export_data(data,command,fileformat,config)

if __name__ == '__main__':
  main()
