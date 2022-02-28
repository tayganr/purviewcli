# pv entity delete
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > delete

## Description
Delete an entity identified by its GUID.

## Syntax
```
pv entity delete --guid=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-by-guid)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}
```

## Examples
Delete an existing entity by its GUID.
```powershell
pv entity delete --guid "d3a5df04-8067-4558-a4bc-01f6ddc5aef8"
```