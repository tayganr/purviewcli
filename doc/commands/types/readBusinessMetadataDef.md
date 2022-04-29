# pv types readBusinessMetadataDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readBusinessMetadataDef

## Description
Get the business metadata definition by GUID or its name (unique).

## Syntax
```
pv types readBusinessMetadataDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the business metadata definition.


`--name` (string)  
The name of the business metadata definition

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get the businessMetadata definition by it's name (unique).](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-business-metadata-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/businessmetadatadef/name/{name}
```

## Examples
Get business metadata definition by name.
```powershell
pv types readBusinessMetadataDef --name "myBizMetadata1"
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
            "isOptional": true,
            "isUnique": false,
            "name": "bizAttr1",
            "options": {
                "applicableEntityTypes": "[\"DataSet\"]",
                "maxStrLength": "50"
            },
            "typeName": "string",
            "valuesMaxCount": 1,
            "valuesMinCount": 0
        }
    ],
    "category": "BUSINESS_METADATA",
    "createTime": 1651150688682,
    "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
    "description": "myBizMetadata1",
    "guid": "8937eb7d-53e3-ce0a-b508-4db55062ed71",
    "lastModifiedTS": "1",
    "name": "myBizMetadata1",
    "typeVersion": "1.0",
    "updateTime": 1651150688682,
    "updatedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
    "version": 1
}
```
</p>
</details>