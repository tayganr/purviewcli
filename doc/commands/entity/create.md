# pv entity create
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > create

## Description
Create or update an entity in Atlas. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array<array>, array<map<string, int>>.

## Syntax
```
pv entity create --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/create-or-update)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity
```

## Examples
```powershell

```