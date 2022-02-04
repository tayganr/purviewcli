# pv relationship read
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > read

## Description
Get relationship information between entities by its GUID.

## Syntax
```
pv relationship read --guid=<val> [--extendedInfo]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the relationship.

## Optional Arguments
`--extendedInfo` (boolean)  
Limits whether includes extended information.

## API Mapping
Catalog Data Plane > Relationship > [Get](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/get)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship/guid/{guid}
```

## Examples
Get relationship information between entities by relationship GUID.
```powershell
pv relationship read --guid "bb990675-2f5b-42aa-a10c-3ce02b5ddf94"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "relationship": {
        "createTime": 1642161843456,
        "createdBy": "ServiceAdmin",
        "end1": {
            "guid": "45e66e18-c22a-4281-bc53-0b573bf84b8c",
            "typeName": "azure_sql_schema",
            "uniqueAttributes": {
                "qualifiedName": "mssql://pvdemofngxi-sqlsvr.database.windows.net/pvdemofngxi-sqldb/SalesLT"
            }
        },
        "end2": {
            "guid": "92b8816a-d0f7-42e6-b840-c4f6f6f60000",
            "typeName": "azure_sql_table",
            "uniqueAttributes": {
                "qualifiedName": "mssql://pvdemofngxi-sqlsvr.database.windows.net/pvdemofngxi-sqldb/SalesLT/Customer"
            }
        },
        "guid": "bb990675-2f5b-42aa-a10c-3ce02b5ddf94",
        "label": "r:azure_sql_schema_tables",
        "lastModifiedTS": "1",
        "propagatedClassifications": [],
        "provenanceType": 0,
        "status": "ACTIVE",
        "typeName": "azure_sql_schema_tables",
        "updateTime": 1642161843456,
        "updatedBy": "ServiceAdmin",
        "version": 0
    }
}
```
</p>
</details>

Include extended information (e.g. referredEntities).
```powershell
pv relationship read --guid "bb990675-2f5b-42aa-a10c-3ce02b5ddf94" --extendedInfo
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "referredEntities": {
        "45e66e18-c22a-4281-bc53-0b573bf84b8c": {
            "attributes": {
                "name": "SalesLT",
                "qualifiedName": "mssql://pvdemofngxi-sqlsvr.database.windows.net/pvdemofngxi-sqldb/SalesLT"
            },
            "classificationNames": [],
            "collectionId": "dtqgax",
            "displayText": "SalesLT",
            "guid": "45e66e18-c22a-4281-bc53-0b573bf84b8c",
            "lastModifiedTS": "1",
            "meaningNames": [],
            "meanings": [],
            "status": "ACTIVE",
            "typeName": "azure_sql_schema"
        },
        "92b8816a-d0f7-42e6-b840-c4f6f6f60000": {
            "attributes": {
                "createTime": 1642161460000,
                "name": "Customer",
                "qualifiedName": "mssql://pvdemofngxi-sqlsvr.database.windows.net/pvdemofngxi-sqldb/SalesLT/Customer"
            },
            "classificationNames": [],
            "collectionId": "dtqgax",
            "displayText": "Customer",
            "guid": "92b8816a-d0f7-42e6-b840-c4f6f6f60000",
            "lastModifiedTS": "1",
            "meaningNames": [],
            "meanings": [],
            "status": "ACTIVE",
            "typeName": "azure_sql_table"
        }
    },
    "relationship": {
        "createTime": 1642161843456,
        "createdBy": "ServiceAdmin",
        "end1": {
            "guid": "45e66e18-c22a-4281-bc53-0b573bf84b8c",
            "typeName": "azure_sql_schema",
            "uniqueAttributes": {
                "qualifiedName": "mssql://pvdemofngxi-sqlsvr.database.windows.net/pvdemofngxi-sqldb/SalesLT"
            }
        },
        "end2": {
            "guid": "92b8816a-d0f7-42e6-b840-c4f6f6f60000",
            "typeName": "azure_sql_table",
            "uniqueAttributes": {
                "qualifiedName": "mssql://pvdemofngxi-sqlsvr.database.windows.net/pvdemofngxi-sqldb/SalesLT/Customer"
            }
        },
        "guid": "bb990675-2f5b-42aa-a10c-3ce02b5ddf94",
        "label": "r:azure_sql_schema_tables",
        "lastModifiedTS": "1",
        "propagatedClassifications": [],
        "provenanceType": 0,
        "status": "ACTIVE",
        "typeName": "azure_sql_schema_tables",
        "updateTime": 1642161843456,
        "updatedBy": "ServiceAdmin",
        "version": 0
    }
}
```
</p>
</details>