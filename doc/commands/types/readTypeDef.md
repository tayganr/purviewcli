# pv types readTypeDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTypeDef

## Description
Get the type definition for the given GUID.

## Syntax
```
pv types readTypeDef (--guid=<val> | --name=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Types > Get Type Definition By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-type-definition-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedef/guid/{guid}
```

## Examples
```powershell

```