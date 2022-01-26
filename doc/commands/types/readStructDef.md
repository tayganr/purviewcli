# pv types readStructDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readStructDef

## Description
Get the struct definition for the given GUID or by its name (unique).

## Syntax
```
pv types readStructDef (--guid=<val> | --name=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Struct Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-struct-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/structdef/guid/{guid}
```

Catalog Data Plane > Types > [Get Struct Def By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-struct-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/structdef/name/{name}
```

## Examples
```powershell

```