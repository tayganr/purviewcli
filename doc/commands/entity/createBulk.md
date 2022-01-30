# pv entity createBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createBulk

## Description
Create or update entities in Atlas in bulk. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array<array>, array<map<string, int>>.

## Syntax
```
pv entity createBulk --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Create Or Update Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/create-or-update-entities)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk
```

## Examples
```powershell

```