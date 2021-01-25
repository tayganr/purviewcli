
"""purviewcli

Usage:
  pv config
  pv search [--keywords=<keywords> --limit=<limit> --offset=<offset> --facet=<facet>...]
  pv assignLabels (--guid=<guid> --label=<label>...)
  pv getEntityAudit (--guid=<guid>) [--auditAction=<auditAction> --count=<count> --startKey=<startKey>]
  pv getEntityBulk (--guid=<guid>...) [--ignoreRelationships --minExtInfo]
  pv deleteEntityBulk (--guid=<guid>...)
  pv getEntityBulkHeaders [--tagUpdateStartTime=<tagUpdateStartTime>]
  pv getEntityBulkUniqueAttributeType (--typeName=<typeName>) [--ignoreRelationships --minExtInfo]
  pv getEntityBusinessmetadataImportTemplate
  pv getEntity (--guid=<guid>) [--ignoreRelationships --minExtInfo]
  pv createEntity (--entityName=<entityName> --entityType=<entityType> --qualifiedName=<qualifiedName>) [--status=<status> --description=<description> --source=<source>]
  pv createEntityBulk (--entityName=<entityName>... --entityType=<entityType>... --qualifiedName=<qualifiedName>...)
  pv deleteEntity (--guid=<guid>)
  pv addEntityClassifications (--guid=<guid> --classificationName=<classificationName>...)
  pv getEntityClassification (--guid=<guid> --classificationName=<classificationName>)
  pv deleteEntityClassification (--guid=<guid> --classificationName=<classificationName>)
  pv getEntityClassifications (--guid=<guid>)
  pv getEntityHeader (--guid=<guid>)
  pv getEntityUniqueAttributeType (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>) [--ignoreRelationships --minExtInfo]
  pv getEntityUniqueAttributeTypeHeader (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>)
  pv getGlossary [--glossaryGuid=<glossaryGuid> --limit=<limit> --offset=<offset> --sort=<sort>]
  pv createGlossary (--name=<name>)
  pv createGlossaryCategory (--categoryName=<name>) [--glossaryGuid=<glossaryGuid>]
  pv createGlossaryCategories (--categoryName=<name>...) [--glossaryGuid=<glossaryGuid>]
  pv getGlossaryTemplate
  pv getGlossaryCategories (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategoriesHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategory (--categoryGuid=<categoryGuid>)
  pv getGlossaryCategoryRelated (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryCategoryTerms (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryDetailed (--glossaryGuid=<glossaryGuid>)
  pv getGlossaryTerm (--termGuid=<termGuid>)
  pv deleteGlossaryTerm (--termGuid=<termGuid>)
  pv purgeGlossaryTerms [--glossaryGuid=<glossaryGuid>]
  pv deleteGlossary (--glossaryGuid=<glossaryGuid>)
  pv deleteGlossaryCategory (--categoryGuid=<categoryGuid>)
  pv deleteAssignedEntities (--termGuid=<termGuid> --guid=<guid>...)
  pv createGlossaryTerm (--termName=<termName>) [--glossaryGuid=<glossaryGuid> --status=<status> --longDescription=<longDescription> --abbreviation=<abbreviation> --synonym=<synonym>... --related=<related>... --resourceName=<resourceName>... --resourceUrl=<resourceUrl>... --expertId=<expertId>... --stewardId=<stewardId>...]
  pv createGlossaryTerms (--termName=<termName>...) [--glossaryGuid=<glossaryGuid> --status=<status>... --longDescription=<longDescription>...]
  pv updateGlossaryTerm (--termGuid=<termGuid>) [--termName=<termName> --glossaryGuid=<glossaryGuid> --status=<status> --longDescription=<longDescription> --abbreviation=<abbreviation> --synonym=<synonym>... --related=<related>... --resourceName=<resourceName>... --resourceUrl=<resourceUrl>... --expertId=<expertId>... --stewardId=<stewardId>...]
  pv getGlossaryTerms (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getAssignedEntities (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv assignEntities (--termGuid=<termGuid> --guid=<guid>...)
  pv getGlossaryTermsHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getGlossaryTermsRelated (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
  pv getLineage (--guid=<guid>) [--depth=<depth> --width=<width> --direction=<direction> --forceNewApi --includeParent --getDerivedLineage]
  pv getLineageUniqueAttributeType (--typeName=<typeName>) [--depth=<depth> --direction=<direction>]
  pv createRelationship (--typeName=<typeName> --status=<status> --end1Guid=<end1Guid> --end2Guid=<end2Guid>)
  pv updateRelationship (--guid=<guid>) [--status=<status> --end1Guid=<end1Guid> --end2Guid=<end2Guid>]
  pv deleteRelationship (--guid=<guid>)
  pv getRelationship (--guid=<guid>) [--extendedInfo]
  pv getBusinessmetadatadef (--guid=<guid> | --name=<name>)
  pv getClassificationdef (--guid=<guid> | --name=<name>)
  pv deleteClassificationdef (--guid=<guid> | --name=<name>)
  pv createClassificationdefs (--defName=<defName>...) [--defDescription=<defDescription>... --defDisplayName=<defDisplayName>...]
  pv updateClassificationdefs (--defName=<defName>...) [--defDescription=<defDescription>... --defDisplayName=<defDisplayName>...]
  pv getEntitydef (--guid=<guid> | --name=<name>)
  pv getEnumdef (--guid=<guid> | --name=<name>)
  pv getRelationshipdef (--guid=<guid> | --name=<name>)
  pv getStructdef (--guid=<guid> | --name=<name>)
  pv getTypedef (--guid=<guid> | --name=<name>)
  pv deleteTypedefName (--name=<name>)
  pv getTypedefs [--type=<type>]
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
  pv getClassificationRules
  pv getClassificationRule (--classificationName=<classificationName>)
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
  --classificationCategory=<classificationCategory> client.
  --classificationName=<classificationName>         client.
  --registeredSourceGroup=<registeredSourceGroup>   client.
  --datasource=<datasource>                         client.
  --fileType=<fileType>                             png or json or csv or xlsx.
  --window=<window>                                 7d or 30d.
  --facet=<facet>                                   Advanced Search.

"""
import sys
import os
import json
from docopt import docopt
from purviewcli import __version__
from purviewcli.client import PurviewClient

def main():
  # Initialise arguments
  args = docopt(__doc__, version=__version__)

  # Initialise client
  client = PurviewClient(account_name = get_var("PURVIEW_NAME"))
  client.set_token()

  function_map = {
    'assignLabels': client.assignLabels,
    'getEntityAudit': client.getEntityAudit,
    'getEntityBulk': client.getEntityBulk,
    'deleteEntityBulk': client.deleteEntityBulk,
    'getEntityBulkHeaders': client.getEntityBulkHeaders,
    'getEntityBulkUniqueAttributeType': client.getEntityBulkUniqueAttributeType,
    'getEntityBusinessmetadataImportTemplate': client.getEntityBusinessmetadataImportTemplate,
    'getEntity': client.getEntity,
    'createEntity': client.createEntity,
    'createEntityBulk': client.createEntityBulk,
    'deleteEntity': client.deleteEntity,
    'getEntityClassification': client.getEntityClassification,
    'deleteEntityClassification': client.deleteEntityClassification,
    'addEntityClassifications': client.addEntityClassifications,
    'getEntityClassifications': client.getEntityClassifications,
    'getEntityHeader': client.getEntityHeader,
    'getEntityUniqueAttributeType': client.getEntityUniqueAttributeType,
    'getEntityUniqueAttributeTypeHeader': client.getEntityUniqueAttributeTypeHeader,
    'getGlossary': client.getGlossary,
    'createGlossary': client.createGlossary,
    'createGlossaryCategory': client.createGlossaryCategory,
    'createGlossaryCategories': client.createGlossaryCategories,
    'getGlossaryTemplate': client.getGlossaryTemplate,
    'getGlossaryCategories': client.getGlossaryCategories,
    'getGlossaryCategoriesHeaders': client.getGlossaryCategoriesHeaders,
    'getGlossaryCategory': client.getGlossaryCategory,
    'getGlossaryCategoryRelated': client.getGlossaryCategoryRelated,
    'getGlossaryCategoryTerms': client.getGlossaryCategoryTerms,
    'getGlossaryDetailed': client.getGlossaryDetailed,
    'getGlossaryTerm': client.getGlossaryTerm,
    'deleteGlossaryTerm': client.deleteGlossaryTerm,
    'purgeGlossaryTerms': client.purgeGlossaryTerms,
    'deleteGlossary': client.deleteGlossary,
    'deleteGlossaryCategory': client.deleteGlossaryCategory,
    'deleteAssignedEntities': client.deleteAssignedEntities,
    'createGlossaryTerm': client.createGlossaryTerm,
    'createGlossaryTerms': client.createGlossaryTerms,
    'updateGlossaryTerm': client.updateGlossaryTerm,
    'getGlossaryTerms': client.getGlossaryTerms,
    'getAssignedEntities': client.getAssignedEntities,
    'assignEntities': client.assignEntities,
    'getGlossaryTermsHeaders': client.getGlossaryTermsHeaders,
    'getGlossaryTermsRelated': client.getGlossaryTermsRelated,
    'getLineage': client.getLineage,
    'getLineageUniqueAttributeType': client.getLineageUniqueAttributeType,
    'getRelationship': client.getRelationship,
    'deleteRelationship': client.deleteRelationship,
    'createRelationship': client.createRelationship,
    'updateRelationship': client.updateRelationship,
    'getBusinessmetadatadef': client.getBusinessmetadatadef,
    'getClassificationdef': client.getClassificationdef,
    'deleteClassificationdef': client.deleteClassificationdef,
    'createClassificationdefs': client.createClassificationdefs,
    'updateClassificationdefs': client.updateClassificationdefs,
    'getEntitydef': client.getEntitydef,
    'getEnumdef': client.getEnumdef,
    'getRelationshipdef': client.getRelationshipdef,
    'getStructdef': client.getStructdef,
    'getTypedef': client.getTypedef,
    'deleteTypedefName': client.deleteTypedefName,
    'getTypedefs': client.getTypedefs,
    'getTypedefsHeaders': client.getTypedefsHeaders,
    'search': client.search,
    'getDatasources': client.getDatasources,
    'getDatasource': client.getDatasource,
    'getScans': client.getScans,
    'getScan': client.getScan,
    'getScanHistory': client.getScanHistory,
    'getScanFilters': client.getScanFilters,
    'runScan': client.runScan,
    'getClassificationRules': client.getClassificationRules,
    'getClassificationRule': client.getClassificationRule,
    'getSystemScanRulesets': client.getSystemScanRulesets,
    'getSystemScanRulesetsSettings': client.getSystemScanRulesetsSettings,
    'getScanRulesets': client.getScanRulesets,
    'getAssetDistributionByDataSource': client.getAssetDistributionByDataSource,
    'getAssetDistributionByTopPaths': client.getAssetDistributionByTopPaths,
    'getFileTypeSizeTimeSeries': client.getFileTypeSizeTimeSeries,
    'getFileTypeSizeTrendByDataSource': client.getFileTypeSizeTrendByDataSource,
    'getTopFileTypesBySize': client.getTopFileTypesBySize,
    'getTopLevelSummary': client.getTopLevelSummary,
    'getRegisteredSourceGroupsWithAssets': client.getRegisteredSourceGroupsWithAssets
  }

  # Execute command
  command = selected_arg(args, function_map.keys())
  func = function_map[command]
  data = func(args)
  
  # Print data
  if len(data) > 0:
    print(json.dumps(data, indent=4, sort_keys=True)) 
  else:
    print('No data found for %s.' % (command))

def selected_arg(args, arg_list):
    selection = None
    for item in  arg_list:
        if args[item]:
            selection = item
    return selection

def get_var(varname):
  varval = os.environ.get(varname)
  if varval is None:
    print("[ERROR] Environment variable '%s' is missing. To set the environment variable, execute the following command: \033[94mexport PURVIEW_NAME=value\033[0m" % varname)
    sys.exit()
  return varval

if __name__ == '__main__':
  main()
