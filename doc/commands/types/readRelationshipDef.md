# pv types readRelationshipDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readRelationshipDef

## Description
Get the relationship definition for the given GUID.

## Syntax
```
pv types readRelationshipDef (--guid=<val> | --name=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Relationship Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-relationship-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/relationshipdef/guid/{guid}
```

## Examples
```powershell

```