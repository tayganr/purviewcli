# pv relationship delete
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > delete

## Description
Delete a relationship between entities by its GUID.

## Syntax
```
pv relationship delete --guid=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Relationship > Delete](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/delete)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship/guid/{guid}
```

## Examples
```powershell

```