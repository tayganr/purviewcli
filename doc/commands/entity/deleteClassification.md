# pv entity deleteClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteClassification

## Description
Delete a given classification from an existing entity represented by a GUID.

## Syntax
```
pv entity deleteClassification --guid=<val> --classificationName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Classification](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-classification)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classification/{classificationName}
```

## Examples
```powershell

```