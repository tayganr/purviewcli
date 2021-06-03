# Azure Purview CLI

This package provides a command line interface to Azure Purview's REST API.  
![purviewcli](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purviewcli_example.png)

## Installation

```
pip install purviewcli
```

## Getting Started

[![YouTube](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purviewcli_youtube.png)](https://www.youtube.com/watch?v=ycr1G5iMM6U)

1. Install purviewcli (e.g. `pip install purviewcli`)
2. Set environment variable(s).
    *  `PURVIEW_NAME` *(mandatory)*
    * `AZURE_CLIENT_ID` *(optional)*
    * `AZURE_TENANT_ID` *(optional)*
    * `AZURE_CLIENT_SECRET` *(optional)*

   Note: The environment variables related to authentication are optional as there are several methods in which we can pass credentials to purviewcli in order to authenticate with an instance of Azure Purview. See [Authentication](#authentication) for more details. 

3. Execute command (e.g. `!pv glossary read`)

Snippet of an example Python-based notebook.


![purviewcli](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purviewcli_notebook.png)

## Authentication

The purviewcli package leverages the `DefaultAzureCredential` method from [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#defaultazurecredential). This provides purviewcli a variety of credential sources it can use to attempt authentication (e.g. Environment Variables, Managed Identity, Visual Studio Code, Azure CLI, Interactive). For example, if you are signed into Azure within Visual Studio Code, purviewcli will leverage those existing credentials when executing a command. This negates the need to store and manage credentials specific to the purviewcli package by leveraging what exists already. Read the [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#defaultazurecredential) documentation to understand the authentication hierarchy.

## Authorization

The identity executing Azure Purview CLI commands will need access to the deployed Azure Purview resource along with the following role assignments:  

* Purview Data Curator
* Purview Data Source Administrator

## Usage

```
pv command sub-command --parameter1='value' --parameter2='value'
```

## Parameter Types

* All parameters are required by default.
* Parameters enclosed with square brackets "**[ ]**" are optional.
* Mutually exclusive parameters are enclosed with parens "**( )**" and separated with a pipe "**|**".
* The "=&lt;val&gt;" indicates parameters which require an input (e.g. --parameter=&lt;val&gt;). Input can be specified after a space (e.g. --parameter 'value') or equal "**=**" sign (e.g. --parameter='value').
* Parameters that do not require an input are **False** by default and **True** if present (e.g. --ignoreRelationships).
* The ellipsis "**...**" indicates parameters that are allowed to repeat (e.g. --guid='12345' --guid='23451' --guid='34512')

## Commands

### Search

```
pv search query [--keywords=<val> --filter-file=<val> --limit=<val> --offset=<val> --facets-file=<val>]
```

### Entity

```
pv entity create --name=<val> --qualifiedName=<val> --typeName=<val> [--description=<val>]
pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
pv entity update --guid=<val> --attrKey=<val> --attrVal=<val>
pv entity delete --guid=<val>
pv entity createBulk --name=<val>... --qualifiedName=<val>... --typeName=<val>...
pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
pv entity readHeader --guid=<val>
pv entity createClassifications --guid=<val> --classificationName=<val>...
pv entity readClassifications --guid=<val>
pv entity readClassification --guid=<val> --classificationName=<val>
pv entity deleteClassification --guid=<val> --classificationName=<val>
pv entity createBulkClassification --classificationName=<val> --guid=<val>...
pv entity readUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val> [--ignoreRelationships --minExtInfo]
pv entity deleteUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val>
pv entity updateUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val> [--description=<val>]
pv entity readBulkUniqueAttributeType --typeName=<val> --attrKey=<val>... --attrVal=<val>... [--ignoreRelationships --minExtInfo]
pv entity createUniqueAttributeTypeClassifications --typeName=<val> --attrKey=<val> --attrVal=<val> --classificationName=<val>...
pv entity updateUniqueAttributeTypeClassifications --typeName=<val> --attrKey=<val> --attrVal=<val> --classificationName=<val>...
pv entity deleteUniqueAttributeTypeClassification --typeName=<val> --attrKey=<val> --attrVal=<val> --classificationName=<val>
```

### Glossary

```
pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val>]
pv glossary create --payload-file=<val>
pv glossary createCategories --payload-file=<val>
pv glossary createCategory --payload-file=<val>
pv glossary deleteCategory --categoryGuid=<val>
pv glossary readCategory --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary putCategory --categoryGuid=<val> --payload-file=<val>
pv glossary putCategoryPartial --categoryGuid=<val> --payload-file=<val>
pv glossary readCategoryRelated --categoryGuid=<val>
pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary createTemplate --payload-file=<val>
pv glossary readTemplate
pv glossary createTerm --payload-file=<val>
pv glossary deleteTerm --termGuid=<val>
pv glossary readTerm --termGuid=<val>
pv glossary putTerm --termGuid=<val> --payload-file=<val>
pv glossary putTermPartial --termGuid=<val> --payload-file=<val>
pv glossary createTerms --payload-file=<val>
pv glossary deleteTermsAssignedEntities --termGuid=<val> --payload-file=<val>
pv glossary readTermsAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary createTermsAssignedEntities --termGuid=<val> --payload-file=<val>
pv glossary putTermsAssignedEntities --termGuid=<val> --payload-file=<val>
pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary delete --glossaryGuid=<val>
pv glossary put --glossaryGuid=<val> --payload-file=<val>
pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary readDetailed --glossaryGuid=<val>
pv glossary putPartial --glossaryGuid=<val> --payload-file=<val>
pv glossary readTerms --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

### Lineage

```
pv lineage read --guid=<val> [--depth=<val> --width=<val> --direction=<val>]
```

### Relationship

```
pv relationship create --typeName=<val> --end1Guid=<val> --end1Type=<val> --end2Guid=<val> --end2Type=<val> [--status=<val>]
pv relationship read --relationshipGuid=<val> [--extendedInfo]
pv relationship update --relationshipGuid=<val> [--status=<val>]
pv relationship delete --relationshipGuid=<val>
```

### Types

```
pv types readTypedefs [--includeTermTemplate --type=<val>]
pv types readTypedefsHeaders [--includeTermTemplate --type=<val>]
pv types readBusinessmetadatadef (--guid=<val> | --name=<val>)
pv types readClassificationdef (--guid=<val> | --name=<val>)
pv types readEntitydef (--guid=<val> | --name=<val>)
pv types readEnumdef (--guid=<val> | --name=<val>)
pv types readRelationshipdef (--guid=<val> | --name=<val>)
pv types readStructdef (--guid=<val> | --name=<val>)
pv types readTypedef (--guid=<val> | --name=<val>)
pv types deleteTypedef --name=<val>
pv types deleteTypedefs --payload-file
pv types createTypedefs --payload-file
pv types putTypedefs --payload-file
```

### Scan

```
pv scan readClassificationRules
pv scan readClassificationRule --classificationRuleName=<val>
pv scan readClassificationRuleVersions --classificationRuleName=<val>
pv scan readDatasources
pv scan readDatasource --dataSourceName=<val>
pv scan readScans --dataSourceName=<val>
pv scan readScan --dataSourceName=<val> --scanName=<val>
pv scan readScanHistory --dataSourceName=<val> --scanName=<val>
pv scan readFilters --dataSourceName=<val> --scanName=<val>
pv scan readTrigger --dataSourceName=<val> --scanName=<val>
pv scan readScanRulesets
pv scan readScanRuleset --scanRulesetName=<val>
pv scan readSystemScanRulesets
pv scan readSystemScanRuleset --dataSourceType=<val>
pv scan readSystemScanRulesetVersion --version=<val> --dataSourceType=<val>
pv scan readSystemScanRulesetLatest --dataSourceType=<val>
pv scan readSystemScanRulesetVersions --dataSourceType=<val>
pv scan readKeyVaults
pv scan readKeyVault --keyVaultName=<val>
pv scan deleteClassificationRule --classificationRuleName=<val>
pv scan deleteDataSource --dataSourceName=<val>
pv scan deleteKeyVault --keyVaultName=<val>
pv scan deleteScanRuleset --scanRulesetName=<val>
pv scan deleteScan --dataSourceName=<val> --scanName=<val>
pv scan deleteTrigger --dataSourceName=<val> --scanName=<val>
pv scan putDataSource --dataSourceName=<val> --payload-file=<val>
pv scan putScan --dataSourceName=<val> --scanName=<val> --payload-file=<val>
pv scan putFilter --dataSourceName=<val> --scanName=<val> --payload-file=<val>
pv scan putTrigger --dataSourceName=<val> --scanName=<val> --payload-file=<val>
pv scan runScan --dataSourceName=<val> --scanName=<val>
pv scan cancelScan --dataSourceName=<val> --scanName=<val> --runId=<val>
pv scan putClassificationRule --classificationRuleName=<val> --payload-file=<val>
pv scan putKeyVault --keyVaultName=<val> --payload-file=<val>
pv scan putScanRuleset --scanRulesetName=<val> --payload-file=<val>
```

### Insight (Guardian)

```
pv insight assetDistributionByDataSource [--registeredSourceGroup=<val> --classificationCategory=<val> --classificationName=<val>]
pv insight assetDistributionByTopPaths --datasource=<val> [--registeredSourceGroup=<val> --classificationCategory=<val> --classificationName=<val>]
pv insight fileTypeSizeTimeSeries --fileType=<val> --window=<val> [--registeredSourceGroup=<val> --datasource=<val>]
pv insight fileTypeSizeTrendByDataSource --fileType=<val> --window=<val> [--registeredSourceGroup=<val> --datasource=<val>]
pv insight topFileTypesBySize [--registeredSourceGroup=<val> --datasource=<val>]
pv insight topLevelSummary [--registeredSourceGroup=<val>]
pv insight registeredSourceGroupsWithAssets
```
