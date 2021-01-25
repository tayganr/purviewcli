# Azure Purview CLI
This package provides a command line interface to Azure Purview's REST API.  
![purviewcli](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purviewcli_example.png)

## Pre-Requisites
The identity executing Azure Purview CLI commands will need access to the deployed Azure Purview resource along with the following role assignments:  
 * Purview Data Curator
 * Purview Data Source Administrator

## Azure Identity
The purviewcli package uses `DefaultAzureCredential` from the [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#defaultazurecredential) library. Read the azure-identity documentation to understand the authentication hierarchy (i.e. Environment Variables > Managed Identity > Visual Studio Code > Azure CLI > Interactive). 

## Environment Variable
Set the PURVIEW_NAME environment variable to the Azure Purview account name.
```
export PURVIEW_NAME=<purview-account-name>
```
Note: Syntax to set an environment variable may vary depending on your environment.

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
**Entity**
```
createEntity (--entityName=<entityName> --entityType=<entityType> --qualifiedName=<qualifiedName>) [--status=<status> --description=<description> --source=<source>]
createEntityBulk (--entityName=<entityName>... --entityType=<entityType>... --qualifiedName=<qualifiedName>...)
getEntity (--guid=<guid>) [--ignoreRelationships --minExtInfo]
getEntityHeader (--guid=<guid>)
getEntityAudit (--guid=<guid>) [--auditAction=<auditAction> --count=<count> --startKey=<startKey>]
getEntityBulk (--guid=<guid>...) [--ignoreRelationships --minExtInfo]
getEntityBulkHeaders [--tagUpdateStartTime=<tagUpdateStartTime>]
getEntityBusinessmetadataImportTemplate
deleteEntity (--guid=<guid>)
deleteEntityBulk (--guid=<guid>...)
```
**Label**
```
assignLabels (--guid=<guid> --label=<label>...)
```
**Classification**
```
addEntityClassifications (--guid=<guid> --classificationName=<classificationName>...)
getEntityClassification (--guid=<guid> --classificationName=<classificationName>)
getEntityClassifications (--guid=<guid>)
deleteEntityClassification (--guid=<guid> --classificationName=<classificationName>)
```
**Unique Attribute**
```
getEntityUniqueAttributeType (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>) [--ignoreRelationships --minExtInfo]
getEntityUniqueAttributeTypeHeader (--typeName=<typeName> --attrKey=<attrKey> --attrVal=<attrVal>)
getEntityBulkUniqueAttributeType (--typeName=<typeName>) [--ignoreRelationships --minExtInfo]
```

### Glossary
**Glossary**
```
createGlossary (--name=<name>)
getGlossary [--glossaryGuid=<glossaryGuid>] [--limit=<limit> --offset=<offset> --sort=<sort>]
getGlossaryDetailed (--glossaryGuid=<glossaryGuid>)
deleteGlossary (--glossaryGuid=<glossaryGuid>)
```

**Category**
```
createGlossaryCategory (--categoryName=<name>) [--glossaryGuid=<glossaryGuid>]
createGlossaryCategories (--categoryName=<name>...) [--glossaryGuid=<glossaryGuid>]
getGlossaryCategory (--categoryGuid=<categoryGuid>)
deleteGlossaryCategory (--categoryGuid=<categoryGuid>)
getGlossaryCategories (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
getGlossaryCategoriesHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
getGlossaryCategoryRelated (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
getGlossaryCategoryTerms (--categoryGuid=<categoryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
```

**Terms**
```
createGlossaryTerm (--termName=<termName>) [--glossaryGuid=<glossaryGuid> --status=<status> --longDescription=<longDescription> --abbreviation=<abbreviation> --synonym=<synonym>... --related=<related>... --resourceName=<resourceName>... --resourceUrl=<resourceUrl>... --expertId=<expertId>... --stewardId=<stewardId>...]
createGlossaryTerms (--termName=<termName>...) [--glossaryGuid=<glossaryGuid> --status=<status>... --longDescription=<longDescription>...]
getGlossaryTerm (--termGuid=<termGuid>)
updateGlossaryTerm (--termGuid=<termGuid>) [--termName=<termName> --glossaryGuid=<glossaryGuid> --status=<status> --longDescription=<longDescription> --abbreviation=<abbreviation> --synonym=<synonym>... --related=<related>... --resourceName=<resourceName>... --resourceUrl=<resourceUrl>... --expertId=<expertId>... --stewardId=<stewardId>...]
deleteGlossaryTerm (--termGuid=<termGuid>)
purgeGlossaryTerms [--glossaryGuid=<glossaryGuid>]
getGlossaryTerms (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
getGlossaryTermsHeaders (--glossaryGuid=<glossaryGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
getGlossaryTermsRelated (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
```

**Assigned Entities**
```
assignEntities (--termGuid=<termGuid> --guid=<guid>...)
getAssignedEntities (--termGuid=<termGuid>) [--limit=<limit> --offset=<offset> --sort=<sort>]
deleteAssignedEntities (--termGuid=<termGuid> --guid=<guid>...)
```

**Template**
```
getGlossaryTemplate
```

### Lineage
**Lineage**
```
getLineage (--guid=<guid>) [--depth=<depth> --width=<width> --direction=<direction> --forceNewApi --includeParent --getDerivedLineage]
getLineageUniqueAttributeType (--typeName=<typeName>) [--depth=<depth> --direction=<direction>]
```
### Relationship
**Relationship**
```
createRelationship (--typeName=<typeName> --status=<status> --end1Guid=<end1Guid> --end2Guid=<end2Guid>)
getRelationship (--guid=<guid>) [--extendedInfo]
updateRelationship (--guid=<guid>) [--status=<status> --end1Guid=<end1Guid> --end2Guid=<end2Guid>]
deleteRelationship (--guid=<guid>)
```
### Types
**Business Metadata Definition**
```
getBusinessmetadatadef (--guid=<guid> | --name=<name>)
```
**Classification Definition**
```
createClassificationdefs (--defName=<defName>...) [--defDescription=<defDescription>... --defDisplayName=<defDisplayName>...]
getClassificationdef (--guid=<guid> | --name=<name>)
updateClassificationdefs (--defName=<defName>...) [--defDescription=<defDescription>... --defDisplayName=<defDisplayName>...]
deleteClassificationdef (--guid=<guid> | --name=<name>)
```
**Entity Definition**
```
getEntitydef (--guid=<guid> | --name=<name>)
```
**Enum Definition**
```
getEnumdef (--guid=<guid> | --name=<name>)
```
**Relationship Definition**
```
getRelationshipdef (--guid=<guid> | --name=<name>)
```
**Struct Definition**
```
getStructdef (--guid=<guid> | --name=<name>)
```
**Type Definition**
```
getTypedef (--guid=<guid> | --name=<name>)
getTypedefs [--type=<type>]
getTypedefsHeaders
deleteTypedefName (--name=<name>)
```

### Scan
```
getDatasources
getDatasource (--datasource=<datasource>)
getScans (--datasource=<datasource>)
getScan (--datasource=<datasource> --scanName=<scanName>)
getScanHistory (--datasource=<datasource> --scanName=<scanName>)
getScanFilters (--datasource=<datasource> --scanName=<scanName>)
runScan (--datasource=<datasource> --scanName=<scanName>) [--scanLevel=<scanLevel>]
getSystemScanRulesets
getSystemScanRulesetsSettings
getScanRulesets
getClassificationRules
getClassificationRule (--classificationName=<classificationName>)
```
### Guardian (Insights)
```
getAssetDistributionByDataSource [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
getAssetDistributionByTopPaths (--datasource=<datasource>) [--registeredSourceGroup=<registeredSourceGroup> --classificationCategory=<classificationCategory> --classificationName=<classificationName>]
getFileTypeSizeTimeSeries (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
getFileTypeSizeTrendByDataSource (--fileType=<fileType> --window=<window>) [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
getTopFileTypesBySize [--registeredSourceGroup=<registeredSourceGroup> --datasource=<datasource>]
getTopLevelSummary [--registeredSourceGroup=<registeredSourceGroup>]
getRegisteredSourceGroupsWithAssets
```
