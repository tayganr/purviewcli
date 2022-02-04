# pv types readStructDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readStructDef

## Description
Get the struct definition for the given GUID or by its name (unique).

## Syntax
```
pv types readStructDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the struct.

`--name` (string)  
The name of the struct.

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
Get struct definition by name.
```powershell
pv types readStructDef --name "cosmosdb_offer"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "attributeDefs": [
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": true,
            "isOptional": false,
            "isUnique": false,
            "name": "content",
            "typeName": "string",
            "valuesMaxCount": 1,
            "valuesMinCount": 1
        },
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": true,
            "isOptional": false,
            "isUnique": false,
            "name": "offerLink",
            "typeName": "string",
            "valuesMaxCount": 1,
            "valuesMinCount": 1
        }
    ],
    "category": "STRUCT",
    "createTime": 1615787946118,
    "createdBy": "admin",
    "description": "cosmosdb_offer",
    "guid": "d96ff541-abd9-a199-58b6-2deb81e4ca5f",
    "lastModifiedTS": "1",
    "name": "cosmosdb_offer",
    "serviceType": "Azure Cosmos DB",
    "typeVersion": "1.0",
    "updateTime": 1615787946118,
    "updatedBy": "admin",
    "version": 1
}
```
</p>
</details>

Get struct definition by guid.
```powershell
pv types readStructDef --guid "d96ff541-abd9-a199-58b6-2deb81e4ca5f"
```