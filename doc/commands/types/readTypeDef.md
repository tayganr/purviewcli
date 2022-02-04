# pv types readTypeDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTypeDef

## Description
Get the type definition for the given GUID or by its name (unique).

## Syntax
```
pv types readTypeDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the type.

`--name` (string)  
The name of the type.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Type Definition By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-type-definition-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedef/guid/{guid}
```

Catalog Data Plane > Types > [Get Type Definition By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-type-definition-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedef/name/{name}
```

## Examples
```powershell

```