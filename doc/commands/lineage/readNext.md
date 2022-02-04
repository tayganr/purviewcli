# pv lineage readNext
[Command Reference](../../../README.md#command-reference) > [lineage](./main.md) > readNext

## Description
Return immediate next page lineage info about entity with pagination.

## Syntax
```
pv lineage readNext --guid=<val> [--direction<val> --offset=<val> --limit=<val>]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity. This needs to be a valid lineage entity type (e.g. adf_copy_operation).

## Optional Arguments
`--direction` (string)  
The direction of the lineage, which could be INPUT, OUTPUT or BOTH.

`--offset` (integer)  
The offset for pagination purpose.

`--limit` (integer)  
The page size - by default there is no paging.

## API Mapping
Catalog Data Plane > Lineage > [Next Page Lineage](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/lineage/next-page-lineage)
```
GET https://{accountName}.purview.azure.com/catalog/api/lineage/{guid}/next
```

## Examples
Get lineage information for a particular entity.
```powershell
pv lineage readNext --guid "c15f00b1-bf72-4413-9e95-565be22d18ed"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "baseEntityGuid": "c15f00b1-bf72-4413-9e95-565be22d18ed",
    "childrenCount": -1,
    "guidEntityMap": {
        "0044971a-b050-4d82-8473-420ee2cf93ec": {
            "attributes": {
                "modifiedTime": 0,
                "name": "QueriesByState",
                "partitionCount": 0,
                "qualifiedName": "https://pvdemofngxiadls.dfs.core.windows.net/bing/data/{N}/QueriesByState_{Year}-{Month}-{Day}_{N}-{N}-{N}.tsv",
                "schemaCount": 0,
                "totalSizeBytes": 0
            },
            "classificationNames": [],
            "collectionId": "yicpjm",
            "displayText": "QueriesByState",
            "guid": "0044971a-b050-4d82-8473-420ee2cf93ec",
            "lastModifiedTS": "2",
            "meaningNames": [],
            "meanings": [],
            "status": "ACTIVE",
            "typeName": "azure_datalake_gen2_resource_set"
        },
        "04f9dca8-e476-439e-8f08-2b6cc7c19f79": {
            "attributes": {
                "modifiedTime": 0,
                "name": "QueriesByCountry",
                "partitionCount": 0,
                "qualifiedName": "https://pvdemofngxiadls.dfs.core.windows.net/bing/data/{N}/QueriesByCountry_{Year}-{Month}-{Day}_{N}-{N}-{N}.tsv",
                "schemaCount": 0,
                "totalSizeBytes": 0
            },
            "classificationNames": [],
            "collectionId": "yicpjm",
            "displayText": "QueriesByCountry",
            "guid": "04f9dca8-e476-439e-8f08-2b6cc7c19f79",
            "lastModifiedTS": "1",
            "meaningNames": [],
            "meanings": [],
            "status": "ACTIVE",
            "typeName": "azure_datalake_gen2_resource_set"
        },
        "900990a3-8d8b-4115-9fe1-403957c90a20": {
            "attributes": {
                "columnMapping": "[{\"DatasetMapping\":{\"Source\":\"*\",\"Sink\":\"https://pvdemofngxiadls.dfs.core.windows.net/bing/data/merged.parquet\"},\"ColumnMapping\":[{\"Source\":\"Date\",\"Sink\":\"Date\"},{\"Source\":\"Query\",\"Sink\":\"Query\"},{\"Source\":\"IsImplicitIntent\",\"Sink\":\"IsImplicitIntent\"},{\"Source\":\"State\",\"Sink\":\"State\"},{\"Source\":\"Country\",\"Sink\":\"Country\"},{\"Source\":\"PopularityScore\",\"Sink\":\"PopularityScore\"}]}]",
                "name": "Copy_a9c",
                "qualifiedName": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvdemo-rg-fngxi/providers/Microsoft.DataFactory/factories/pvdemofngxi-adf/pipelines/copyPipeline_copy1/activities/Copy_a9c#https://pvdemofngxiadls.dfs.core.windows.net/bing/data/merged.parquet#azure_datalake_gen2_path"
            },
            "classificationNames": [],
            "displayText": "Copy_a9c",
            "guid": "900990a3-8d8b-4115-9fe1-403957c90a20",
            "lastModifiedTS": "12",
            "meaningNames": [],
            "meanings": [],
            "status": "ACTIVE",
            "typeName": "adf_copy_operation"
        },
        "d4faadd8-a815-40b9-aaad-c782f96aa4c5": {
            "attributes": {
                "contentType": "application/octet-stream",
                "groups": "$superuser",
                "isFile": true,
                "modifiedTime": 1642162417000,
                "name": "merged.parquet",
                "owner": "6b854594-92ad-4a03-b209-7413af34e6c2",
                "path": "/bing/data/merged.parquet",
                "qualifiedName": "https://pvdemofngxiadls.dfs.core.windows.net/bing/data/merged.parquet",
                "size": 175123065
            },
            "classificationNames": [
                "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
            ],
            "collectionId": "yicpjm",
            "displayText": "merged.parquet",
            "guid": "d4faadd8-a815-40b9-aaad-c782f96aa4c5",
            "lastModifiedTS": "4",
            "meaningNames": [],
            "meanings": [],
            "status": "ACTIVE",
            "typeName": "azure_datalake_gen2_path"
        }
    },
    "includeParent": false,
    "lineageDepth": 1,
    "lineageDirection": "BOTH",
    "lineageWidth": -1,
    "relations": [
        {
            "fromEntityId": "900990a3-8d8b-4115-9fe1-403957c90a20",
            "relationshipId": "ef3d6537-e4a6-4afe-a104-48244fb28743",
            "toEntityId": "d4faadd8-a815-40b9-aaad-c782f96aa4c5"
        },
        {
            "fromEntityId": "04f9dca8-e476-439e-8f08-2b6cc7c19f79",
            "relationshipId": "6c0ad293-9003-4709-8f5c-a19965b33542",
            "toEntityId": "900990a3-8d8b-4115-9fe1-403957c90a20"
        },
        {
            "fromEntityId": "0044971a-b050-4d82-8473-420ee2cf93ec",
            "relationshipId": "7031244b-9139-41dc-8536-921093b154b9",
            "toEntityId": "900990a3-8d8b-4115-9fe1-403957c90a20"
        }
    ],
    "widthCounts": {
        "BOTH": null
    }
}
```
</p>
</details>