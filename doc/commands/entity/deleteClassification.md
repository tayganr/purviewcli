# pv entity deleteClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteClassification

## Description
Delete a given classification from an existing entity represented by a GUID.

## Syntax
```
pv entity deleteClassification --guid=<val> --classificationName=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--classificationName` (string)  
The name of the classification.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Classification](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-classification)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classification/{classificationName}
```

## Examples
Remove a classification from an entity via the entity GUID.
```powershell
pv entity deleteClassification --guid "bbb9ff1d-f880-435e-ac87-d6fd5676d8f0" --classificationName "MICROSOFT.FINANCIAL.CREDIT_CARD_NUMBER"
```