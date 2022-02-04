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
Get relationship definition by name.
```powershell
pv types readRelationshipDef --name "bigquery_dataset_tables"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "attributeDefs": [],
    "category": "RELATIONSHIP",
    "createTime": 1615887114341,
    "createdBy": "admin",
    "description": "bigquery_dataset_tables",
    "endDef1": {
        "cardinality": "SET",
        "isContainer": true,
        "isLegacyAttribute": false,
        "name": "tables",
        "type": "bigquery_dataset"
    },
    "endDef2": {
        "cardinality": "SINGLE",
        "isContainer": false,
        "isLegacyAttribute": false,
        "name": "dataset",
        "type": "bigquery_table"
    },
    "guid": "94dced37-45a9-7660-f63d-fd2ab949da82",
    "lastModifiedTS": "1",
    "name": "bigquery_dataset_tables",
    "propagateTags": "NONE",
    "relationshipCategory": "COMPOSITION",
    "serviceType": "Google BigQuery",
    "typeVersion": "1.0",
    "updateTime": 1615887114341,
    "updatedBy": "admin",
    "version": 1
}
```
</p>
</details>

Get relationship definition by guid.
```powershell
pv types readRelationshipDef --guid "94dced37-45a9-7660-f63d-fd2ab949da82"
```