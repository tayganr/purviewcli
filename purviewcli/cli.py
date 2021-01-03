
"""purviewcli

Usage:
  purviewcli config
  purviewcli [csv | json] search (--keywords=<keywords>) [--limit=<limit> --offset=<offset>]
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
  purviewcli [csv | json] newGlossaryTerm (--termName=<termName> --termStatus=<termStatus>) [--termDescription=<termDescription> --termAcronym=<termAcronym> --synonym=<synonym>... --related=<related>...]
  purviewcli [csv | json] getGlossaryTerms (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryTermsAssignedEntities (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryTermsHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getGlossaryTermsRelated (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  purviewcli [csv | json] getLineage (--guid=<guid>) [--depth=<depth> --width=<width> --direction=<direction> --forceNewApi --includeParent --getDerivedLineage]
  purviewcli [csv | json] getLineageUniqueAttributeType (--typeName=<typeName>) [--depth=<depth> --direction=<direction>]
  purviewcli [csv | json] getRelationshipGuid (--guid=<guid>) [--extendedInfo]
  purviewcli [csv | json] getBusinessmetadatadef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getClassificationdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getEntitydef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getEnumdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getRelationshipdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getStructdef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypedef (--guid=<guid> | --name=<name>)
  purviewcli [csv | json] getTypedefs
  purviewcli [csv | json] getTypedefsHeaders
  purviewcli [csv | json] getDatasources
  purviewcli [csv | json] getDatasource (--datasource=<datasource>)
  purviewcli [csv | json] getScans (--datasource=<datasource>)
  purviewcli [csv | json] getScan (--datasource=<datasource> --scanName=<scanName>)
  purviewcli [csv | json] getScanHistory (--datasource=<datasource> --scanName=<scanName>)
  purviewcli [csv | json] getScanFilters (--datasource=<datasource> --scanName=<scanName>)
  purviewcli [csv | json] runScan (--datasource=<datasource> --scanName=<scanName>) [--scanLevel=<scanLevel>]
  purviewcli [csv | json] getSystemScanRulesets
  purviewcli [csv | json] getSystemScanRulesetsSettings
  purviewcli [csv | json] getScanRulesets
  purviewcli [csv | json] getAssetDistributionByDataSource [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
  purviewcli [csv | json] getAssetDistributionByTopPaths (--datasource=<datasource>) [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
  purviewcli [csv | json] getFileTypeSizeTimeSeries (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
  purviewcli [csv | json] getFileTypeSizeTrendByDataSource (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
  purviewcli [csv | json] getTopFileTypesBySize [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
  purviewcli [csv | json] getTopLevelSummary [--registeredSourceGroup=<registeredSourceGroup>]
  purviewcli [csv | json] getRegisteredSourceGroupsWithAssets

Options:
  -h --help                                         Show this screen.
  -v --version                                      Show version.
  --limit=<limit>                                   By default there is no paging [default: -1].
  --offset=<offset>                                 Offset for pagination purpose [default: 0].
  --sort=<sort>                                     ASC or DESC [default: ASC].
  --auditAction=<auditAction>                       BUSINESS_ATTRIBUTE_UPDATE or CLASSIFICATION_ADD or CLASSIFICATION_DELETE or CLASSIFICATION_UPDATE or ENTITY_CREATE or ENTITY_DELETE or ENTITY_IMPORT_CREATE or ENTITY_IMPORT_DELETE or ENTITY_IMPORT_UPDATE or ENTITY_PURGE or ENTITY_UPDATE or LABEL_ADD or LABEL_DELETE or PROPAGATED_CLASSIFICATION_ADD or PROPAGATED_CLASSIFICATION_DELETE or PROPAGATED_CLASSIFICATION_UPDATE or TERM_ADD or TERM_DELETE.
  --count=<count>                                   Number of events required	[default: 100].
  --startKey=<startKey>                             Used for pagination. Startkey is inclusive, the returned results contain the event with the given startkey.
  --tagUpdateStartTime=<tagUpdateStartTime>         DataType long.
  --depth=<depth>                                   Number of hops for lineage [default: 3].
  --width=<width>                                   Custom to Azure Purview [default: 6].
  --direction=<direction>                           INPUT or OUTPUT or BOTH [default: BOTH].
  --scanLevel=<scanLevel>                           Incremental or Full.
  --registeredSourceGroup=<registeredSourceGroup>   Guardian.
  --classificationCategory=<classificationCategory> Guardian.
  --classificationName=<classificationName>         Guardian.
  --fileType=<fileType>                             png or json or csv or xlsx.
  --window=<window>                                 7d or 30d.

"""
from docopt import docopt
from purviewcli import __version__
from purviewcli import common
from purviewcli import entity
from purviewcli import glossary
from purviewcli import lineage
from purviewcli import relationship
from purviewcli import typedefs
from purviewcli import search
from purviewcli import scan
from purviewcli import guardian

def main():
  # Initialise Arguments (docopt)
  args = docopt(__doc__, version=__version__)
  # print(args)
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
    'newGlossaryTerm': glossary.newGlossaryTerm,
    'getGlossaryTerms': glossary.getGlossaryTerms,
    'getGlossaryTermsAssignedEntities': glossary.getGlossaryTermsAssignedEntities,
    'getGlossaryTermsHeaders': glossary.getGlossaryTermsHeaders,
    'getGlossaryTermsRelated': glossary.getGlossaryTermsRelated,
    'getLineage': lineage.getLineage,
    'getLineageUniqueAttributeType': lineage.getLineageUniqueAttributeType,
    'getRelationshipGuid': relationship.getRelationshipGuid,
    'getBusinessmetadatadef': typedefs.getBusinessmetadatadef,
    'getClassificationdef': typedefs.getClassificationdef,
    'getEntitydef': typedefs.getEntitydef,
    'getEnumdef': typedefs.getEnumdef,
    'getRelationshipdef': typedefs.getRelationshipdef,
    'getStructdef': typedefs.getStructdef,
    'getTypedef': typedefs.getTypedef,
    'getTypedefs': typedefs.getTypedefs,
    'getTypedefsHeaders': typedefs.getTypedefsHeaders,
    'search': search.search,
    'getDatasources': scan.getDatasources,
    'getDatasource': scan.getDatasource,
    'getScans': scan.getScans,
    'getScan': scan.getScan,
    'getScanHistory': scan.getScanHistory,
    'getScanFilters': scan.getScanFilters,
    'runScan': scan.runScan,
    'getSystemScanRulesets': scan.getSystemScanRulesets,
    'getSystemScanRulesetsSettings': scan.getSystemScanRulesetsSettings,
    'getScanRulesets': scan.getScanRulesets,
    'getAssetDistributionByDataSource': guardian.getAssetDistributionByDataSource,
    'getAssetDistributionByTopPaths': guardian.getAssetDistributionByTopPaths,
    'getFileTypeSizeTimeSeries': guardian.getFileTypeSizeTimeSeries,
    'getFileTypeSizeTrendByDataSource': guardian.getFileTypeSizeTrendByDataSource,
    'getTopFileTypesBySize': guardian.getTopFileTypesBySize,
    'getTopLevelSummary': guardian.getTopLevelSummary,
    'getRegisteredSourceGroupsWithAssets': guardian.getRegisteredSourceGroupsWithAssets
  }

  config = common.read_config()
  command = common.selected_arg(args, function_map.keys())
  func = function_map[command]
  data = func(config, args)
  fileformat = common.selected_arg(args, ['csv','json'])
  common.export_data(data,command,fileformat,config)

if __name__ == '__main__':
  main()
