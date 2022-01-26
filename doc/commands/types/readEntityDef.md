# pv types readEntityDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readEntityDef

## Description
Get the Entity definition for the given GUID or by its name (unique).

## Syntax
```
pv types readEntityDef (--guid=<val> | --name=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Entity Definition By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-entity-definition-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/entitydef/guid/{guid}
```

Catalog Data Plane > Types > [Get Entity Definition By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-entity-definition-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/entitydef/name/{name}
```

## Examples
```powershell

```