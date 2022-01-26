# pv entity readClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readClassifications

## Description
List classifications for a given entity represented by a GUID.

## Syntax
```
pv entity readClassifications --guid=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-classifications)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classifications
```

## Examples
```powershell

```