# pv entity deleteBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteBulk

## Description
Delete a list of entities in bulk identified by their GUIDs or unique attributes.

## Syntax
```
pv entity deleteBulk --guid=<val>...
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete By Guids](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-by-guids)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk
```

## Examples
```powershell

```