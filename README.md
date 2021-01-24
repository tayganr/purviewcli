# Azure Purview CLI
This package provides a command line interface to Azure Purview's REST API.  
![purviewcli](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purviewcli_example.png)

## Pre-Requisites
The identity executing Azure Purview CLI commands will need access to the deployed Azure Purview resource along with the following role assignments:  
 * Purview Data Curator
 * Purview Data Source Administrator

## Environment Variable
Set the PURVIEW_NAME environment variable to the Azure Purview account name.
```
export PURVIEW_NAME=<purview-account-name>
```

## Installation
```
pip install purviewcli
```

## Usage
```
pv command (mandatory parameters) [optional parameters]
```

## Commands
### Search
```
pv search [--keywords=<keywords> --limit=<limit> --offset=<offset> --facet=<facet>...]
```
### Entity
```
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
```
### Glossary
```
pv getGlossary [--glossaryGuid=<glossaryGuid>] [--limit=<limit> --offset=<offset> --sort=<sort>]
pv createGlossary (--name=<name>)
pv createGlossaryCategory (--name=<name> --glossaryGuid=<glossaryGuid>)
pv getGlossaryTemplate
pv getGlossaryCategories (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv getGlossaryCategoriesHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv getGlossaryCategory (--categoryGuid=<categoryGuid>)
pv getGlossaryCategoryRelated (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv getGlossaryCategoryTerms (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv getGlossaryDetailed (--glossaryGuid=<glossaryGuid>)
pv getGlossaryTerm (--termGuid=<termGuid>)
pv deleteGlossaryTerm (--termGuid=<termGuid>)
pv deleteGlossary (--glossaryGuid=<glossaryGuid>)
pv deleteGlossaryCategory (--categoryGuid=<categoryGuid>)
pv deleteAssignedEntities (--termGuid=<termGuid> --guid=<guid>...)
pv createGlossaryTerm (--termName=<termName>) [--glossaryGuid=<glossaryGuid> --status=<status> --longDescription=<longDescription> --abbreviation=<abbreviation> --synonym=<synonym>... --related=<related>... --resourceName=<resourceName>... --resourceUrl=<resourceUrl>... --expertId=<expertId>... --stewardId=<stewardId>...]
pv updateGlossaryTerm (--termGuid=<termGuid>) [--termName=<termName> --glossaryGuid=<glossaryGuid> --status=<status> --longDescription=<longDescription> --abbreviation=<abbreviation> --synonym=<synonym>... --related=<related>... --resourceName=<resourceName>... --resourceUrl=<resourceUrl>... --expertId=<expertId>... --stewardId=<stewardId>...]
pv getGlossaryTerms (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv getAssignedEntities (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv assignEntities (--termGuid=<termGuid> --guid=<guid>...)
pv getGlossaryTermsHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
pv getGlossaryTermsRelated (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
```
### Lineage
```
pv getLineage (--guid=<guid>) [--depth=<depth> --width=<width> --direction=<direction> --forceNewApi --includeParent --getDerivedLineage]
pv getLineageUniqueAttributeType (--typeName=<typeName>) [--depth=<depth> --direction=<direction>]
```
### Relationship
```
pv createRelationship (--typeName=<typeName> --status=<status> --end1Guid=<end1Guid> --end2Guid=<end2Guid>)
pv updateRelationship (--guid=<guid>) [--status=<status> --end1Guid=<end1Guid> --end2Guid=<end2Guid>]
pv deleteRelationship (--guid=<guid>)
pv getRelationship (--guid=<guid>) [--extendedInfo]
```
### Types
```
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
```
### Scan
```
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
```
### Guardian (Insights)
```
pv getAssetDistributionByDataSource [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
pv getAssetDistributionByTopPaths (--datasource=<datasource>) [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
pv getFileTypeSizeTimeSeries (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
pv getFileTypeSizeTrendByDataSource (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
pv getTopFileTypesBySize [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
pv getTopLevelSummary [--registeredSourceGroup=<registeredSourceGroup>]
pv getRegisteredSourceGroupsWithAssets
```
