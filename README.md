# Azure Purview CLI
This package provides a command line interface to Azure Purview's REST API.

## Pre-Requisites
1. An [Azure Purview](https://docs.microsoft.com/en-us/azure/purview/create-catalog-portal) account.
2. A [Service Principal](https://docs.microsoft.com/en-us/azure/purview/tutorial-using-rest-apis#create-a-service-principal-application) (Azure AD application). 
3. Grant Service Principal [role assignment](https://docs.microsoft.com/en-us/azure/purview/tutorial-using-rest-apis#configure-your-catalog-to-trust-the-service-principal-application) *(Azure Purview > Access Control (IAM) > Add role assignment > Purview Data Curator)*.

## Installation
```
pip install purviewcli
```

## Configuration
You will need the following to initialise the configuration file:
* Client ID *(aka Application ID)*
* Client Secret
* Tenant ID *(aka Directory ID)*
* Azure Purview Account Name
* Output Path *(e.g. Windows: C:/Users/username/Desktop Mac: /Users/username/Desktop)*

To initiate the configuration, execute the following command.
```
purviewcli config
```

## Usage
```
purviewcli command (mandatory parameters) [optional parameters]
```

## Commands
  config  
  getEntityAudit (--guid=&lt;guid&gt;) [--auditAction=&lt;auditAction&gt; --count=&lt;count&gt; --startKey=&lt;startKey&gt;]  
  getEntityBulk (--guid=&lt;guid&gt;...) [--ignoreRelationships --minExtInfo]  
  getEntityBulkHeaders [--tagUpdateStartTime=&lt;tagUpdateStartTime&gt;]  
  getEntityBulkUniqueAttributeType (--typeName=&lt;typeName&gt;) [--ignoreRelationships --minExtInfo]  
  getEntityBusinessmetadataImportTemplate  
  getEntityGuid (--guid=&lt;guid&gt;) [--ignoreRelationships --minExtInfo]  
  getEntityGuidClassification (--guid=&lt;guid&gt; --classificationName=&lt;classificationName&gt;)  
  getEntityGuidClassifications (--guid=&lt;guid&gt;)  
  getEntityGuidHeader (--guid=&lt;guid&gt;)  
  getEntityUniqueAttributeType (--typeName=&lt;typeName&gt; --attrKey=&lt;attrKey&gt; --attrVal=&lt;attrVal&gt;) [--ignoreRelationships --minExtInfo]  
  getEntityUniqueAttributeTypeHeader (--typeName=&lt;typeName&gt; --attrKey=&lt;attrKey&gt; --attrVal=&lt;attrVal&gt;)  
  getGlossary [--glossaryGuid=&lt;glossaryGuid&gt;] [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryCategories (--glossaryGuid=&lt;glossaryGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryCategoriesHeaders (--glossaryGuid=&lt;glossaryGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryCategory (--categoryGuid=&lt;categoryGuid&gt;)  
  getGlossaryCategoryRelated (--categoryGuid=&lt;categoryGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryCategoryTerms (--categoryGuid=&lt;categoryGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryDetailed (--glossaryGuid=&lt;glossaryGuid&gt;)  
  getGlossaryTerm (--termGuid=&lt;termGuid&gt;)  
  getGlossaryTerms (--glossaryGuid=&lt;glossaryGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryTermsAssignedEntities (--termGuid=&lt;termGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryTermsHeaders (--glossaryGuid=&lt;glossaryGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getGlossaryTermsRelated (--termGuid=&lt;termGuid&gt;) [--limit=&lt;limit&gt; --offset=&lt;offset&gt; --sort=&lt;sort&gt;]  
  getLineage (--guid=&lt;guid&gt;) [--depth=&lt;depth&gt; --width=&lt;width&gt; --direction=&lt;direction&gt; --forceNewApi --includeParent --getDerivedLineage]  
  getLineageUniqueAttributeType (--typeName=&lt;typeName&gt;) [--depth=&lt;depth&gt; --direction=&lt;direction&gt;]  
  getRelationshipGuid (--guid=&lt;guid&gt;) [--extendedInfo]  
  getTypesBusinessmetadatadef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesClassificationdef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesEntitydef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesEnumdef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesRelationshipdef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesStructdef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesTypedef (--guid=&lt;guid&gt; | --name=&lt;name&gt;)  
  getTypesTypedefs  
  getTypesTypedefsHeaders  

Options:
| Option        | Description   |
| ------------- | ------------- |
| -h --help                           | Show this screen. |
| -v --version                        | Show version. |
|--limit=&lt;limit&gt;                | Page size, by default there is no paging [default: -1]. |
| --offset=&lt;offset&gt;             | Offset for pagination purpose [default: 0]. |
| --sort=&lt;sort&gt;                 | ASC or DESC [default: ASC]. |
| --auditAction=&lt;auditAction&gt;   | BUSINESS_ATTRIBUTE_UPDATE or CLASSIFICATION_ADD or  CLASSIFICATION_DELETE or C LASSIFICATION_UPDATE or ENTITY_CREATE or ENTITY_DELETE or ENTITY_IMPORT_CREATE or ENTITY_IMPORT_DELETE or ENTITY_IMPORT_UPDATE or ENTITY_PURGE or ENTITY_UPDATE or LABEL_ADD or LABEL_DELETE or PROPAGATED_CLASSIFICATION_ADD or PROPAGATED_CLASSIFICATION_DELETE or PROPAGATED_CLASSIFICATION_UPDATE or TERM_ADD or TERM_DELETE.|
| --count=&lt;count&gt;               | Number of events required [default: 100]. |
| --startKey=&lt;startKey&gt;         | Used for pagination. Startkey is inclusive, the returned results contain the event with the given startkey. |
| --tagUpdateStartTime=&lt;tagUpdateStartTime&gt;   | DataType long. |
| --depth=&lt;depth&gt;               | Number of hops for lineage [default: 3]. |
| --width=&lt;width&gt;               | Custom to Azure Purview [default: 6]. |
| --direction=&lt;direction&gt;       | INPUT or OUTPUT or BOTH [default: BOTH]. |


## Export to JSON
```
purviewcli json command (mandatory parameters) [optional parameters]
```

## Export to CSV
```
purviewcli csv command (mandatory parameters) [optional parameters]
```