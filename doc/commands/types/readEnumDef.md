# pv types readEnumDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readEnumDef

## Description
Get the enum definition for the given GUID or by its name (unique).

## Syntax
```
pv types readEnumDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the enum.

`--name` (string)  
The name of the enum.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Enum Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-enum-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/enumdef/guid/{guid}
```

Catalog Data Plane > Types > [Get Enum Def By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-enum-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/enumdef/name/{name}
```

## Examples
Get
```powershell
pv types readEntityDef --name "azure_sql_table"
```

Get 
```powershell
pv types readEntityDef --guid "7d92a449-f7e8-812f-5fc8-ca6127ba90bd"
```