# pv entity delete
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > delete

## Description
Delete an entity identified by its GUID.

## Syntax
```
pv entity delete --guid=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-by-guid)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}
```

## Examples
```powershell

```