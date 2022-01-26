# pv entity readClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readClassification

## Description
List classifications for a given entity represented by a GUID.

## Syntax
```
pv entity readClassification --guid=<val> --classificationName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Entity > Get Classification](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-classification)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classification/{classificationName}
```

## Examples
```powershell

```