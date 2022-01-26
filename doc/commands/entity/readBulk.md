# pv entity readBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readBulk

## Description
List entities in bulk identified by its GUIDs.

## Syntax
```
pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [List By Guids](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/list-by-guids)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk
```

## Examples
```powershell

```