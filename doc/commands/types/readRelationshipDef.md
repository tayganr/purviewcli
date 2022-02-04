# pv types readRelationshipDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readRelationshipDef

## Description
Get the relationship definition for the given GUID or by its name (unique).

## Syntax
```
pv types readRelationshipDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the relationship.

`--name` (string)  
The name of the relationship.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Relationship Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-relationship-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/relationshipdef/guid/{guid}
```

Catalog Data Plane > Types > [Get Relationship Def By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-relationship-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/relationshipdef/name/{name}
```

## Examples
```powershell

```