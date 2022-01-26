# pv entity read
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > read

## Description
Get complete definition of an entity given its GUID.

## Syntax
```
pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}
```

## Examples
```powershell

```