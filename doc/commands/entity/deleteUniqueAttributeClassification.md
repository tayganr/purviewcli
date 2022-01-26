# pv entity deleteUniqueAttributeClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteUniqueAttributeClassification

## Description
Delete a given classification from an entity identified by its type and unique attributes.

## Syntax
```
pv entity deleteUniqueAttributeClassification --typeName=<val> --classificationName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Classification By Unique Attribute](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-classification-by-unique-attribute)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classification/{classificationName}
```

## Examples
```powershell

```