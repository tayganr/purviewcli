
"""purviewcli

Usage:
  pv config
  pv search (--keywords=<keywords>) [--limit=<limit> --offset=<offset>]
  pv getEntityAudit (--guid=<guid>) [--auditAction=<auditAction> --count=<count> --startKey=<startKey>]
  pv getEntityBulk (--guid=<guid>...) [--ignoreRelationships --minExtInfo]
  pv getEntityBulkHeaders [--tagUpdateStartTime=<tagUpdateStartTime>]
  pv getEntityBulkUniqueAttributeType (--typeName=<typeName>) [--ignoreRelationships --minExtInfo]
  pv getEntityBusinessmetadataImportTemplate
  pv getEntityGuid (--guid=<guid>) [--ignoreRelationships --minExtInfo]
  pv getEntityGuidClassification (--guid=<guid> --classificationName=<classificationName>)
  pv getEntityGuidClassifications (--guid=<guid>)
  pv getEntityGuidHeader (--guid=<guid>)
  pv getEntityUniqueAttributeType (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>) [--ignoreRelationships --minExtInfo]
  pv getEntityUniqueAttributeTypeHeader (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>)
  pv getGlossary [--glossaryGuid=<glossaryGuid>] [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategories (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategoriesHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategory (--categoryGuid=<categoryGuid>)
  pv getGlossaryCategoryRelated (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategoryTerms (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryDetailed (--glossaryGuid=<glossaryGuid>)
  pv getGlossaryTerm (--termGuid=<termGuid>)
  pv newGlossaryTerm (--termName=<termName> --termStatus=<termStatus>) [--termDescription=<termDescription> --termAcronym=<termAcronym> --synonym=<synonym>... --related=<related>...]
  pv getGlossaryTerms (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryTermsAssignedEntities (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryTermsHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryTermsRelated (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getLineage (--guid=<guid>) [--depth=<depth> --width=<width> --direction=<direction> --forceNewApi --includeParent --getDerivedLineage]
  pv getLineageUniqueAttributeType (--typeName=<typeName>) [--depth=<depth> --direction=<direction>]
  pv getRelationshipGuid (--guid=<guid>) [--extendedInfo]
  pv getBusinessmetadatadef (--guid=<guid> | --name=<name>)
  pv getClassificationdef (--guid=<guid> | --name=<name>)
  pv getEntitydef (--guid=<guid> | --name=<name>)
  pv getEnumdef (--guid=<guid> | --name=<name>)
  pv getRelationshipdef (--guid=<guid> | --name=<name>)
  pv getStructdef (--guid=<guid> | --name=<name>)
  pv getTypedef (--guid=<guid> | --name=<name>)
  pv getTypedefs
  pv getTypedefsHeaders
  pv getDatasources
  pv getDatasource (--datasource=<datasource>)
  pv getScans (--datasource=<datasource>)
  pv getScan (--datasource=<datasource> --scanName=<scanName>)
  pv getScanHistory (--datasource=<datasource> --scanName=<scanName>)
  pv getScanFilters (--datasource=<datasource> --scanName=<scanName>)
  pv runScan (--datasource=<datasource> --scanName=<scanName>) [--scanLevel=<scanLevel>]
  pv getSystemScanRulesets
  pv getSystemScanRulesetsSettings
  pv getScanRulesets
  pv getAssetDistributionByDataSource [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
  pv getAssetDistributionByTopPaths (--datasource=<datasource>) [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
  pv getFileTypeSizeTimeSeries (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
  pv getFileTypeSizeTrendByDataSource (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
  pv getTopFileTypesBySize [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
  pv getTopLevelSummary [--registeredSourceGroup=<registeredSourceGroup>]
  pv getRegisteredSourceGroupsWithAssets

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
  --classificationCategory=<classificationCategory> Guardian.
  --classificationName=<classificationName>         Guardian.
  --registeredSourceGroup=<registeredSourceGroup>   Guardian.
  --datasource=<datasource>                         Guardian.
  --fileType=<fileType>                             png or json or csv or xlsx.
  --window=<window>                                 7d or 30d.

"""
import json
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
  args = docopt(__doc__, version=__version__)

  # Special Argument: config
  if args['config']:
    common.init_config()
  else:
    purview_api(args)

def purview_api(args):
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
  
  if len(data) > 0:
    print(json.dumps(data, indent=4, sort_keys=True)) 
  else:
    print('No data found for %s.' % (command))

if __name__ == '__main__':
  main()
