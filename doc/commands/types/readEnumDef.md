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
Get enum definition by name.
```powershell
pv types readEnumDef --name "blob_type"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "category": "ENUM",
    "createTime": 1615787945788,
    "createdBy": "admin",
    "description": "blob_type",
    "elementDefs": [
        {
            "ordinal": 0,
            "value": "Unspecified"
        },
        {
            "ordinal": 1,
            "value": "PageBlob"
        },
        {
            "ordinal": 2,
            "value": "BlockBlob"
        },
        {
            "ordinal": 3,
            "value": "AppendBlob"
        }
    ],
    "guid": "171bba26-3a17-3f5c-50f2-1e313c87d473",
    "lastModifiedTS": "1",
    "name": "blob_type",
    "serviceType": "Azure Blob Storage",
    "typeVersion": "1.0",
    "updateTime": 1615787945788,
    "updatedBy": "admin",
    "version": 1
}
```
</p>
</details>

Get enum definition by guid.
```powershell
pv types readEnumDef --guid "171bba26-3a17-3f5c-50f2-1e313c87d473"
```