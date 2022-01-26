# pv entity readHeader
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readHeader

## Description
Get entity header given its GUID.

## Syntax
```
pv entity readHeader --guid=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Header](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-header)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/header
```

## Examples
```powershell

```