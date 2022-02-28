# pv entity deleteUniqueAttributeClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteUniqueAttributeClassification

## Description
Delete a given classification from an entity identified by its type and unique attributes.

## Syntax
```
pv entity deleteUniqueAttributeClassification --typeName=<val> --qualifiedName=<val> --classificationName=<val>
```

## Required Arguments
`--typeName` (string)  
The name of the type.

`--qualifiedName` (string)  
The qualified name of the entity.

`--classificationName` (string)  
The name of the classification.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Classification By Unique Attribute](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-classification-by-unique-attribute)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classification/{classificationName}
```

## Examples
Remove a classification from an entity via the entities qualified name.
```powershell
pv entity deleteUniqueAttributeClassification --typeName "azure_datalake_gen2_filesystem" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/02-silver" --classificationName "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
```