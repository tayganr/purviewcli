# pv entity readBulkUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readBulkUniqueAttribute

## Description
Bulk API to retrieve list of entities identified by its unique attributes.

## Syntax
```
pv entity readBulkUniqueAttribute --typeName=<val> --qualifiedName=<val>... [--ignoreRelationships --minExtInfo]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Entities By Unique Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-entities-by-unique-attributes)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk/uniqueAttribute/type/{typeName}
```

## Examples
Get the complete definition for a list of existing entities (bulk) by specifying a type name and a list of qualified names.
```powershell
pv entity readBulkUniqueAttribute --typeName "azure_datalake_gen2_path" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/xyz_company.csv" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/filename.csv"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "entities": [
        {
            "attributes": {
                "ACL": null,
                "contentType": "application/octet-stream",
                "description": null,
                "groups": "$superuser",
                "isFile": true,
                "modifiedTime": 1645630994000,
                "name": "xyz_company.csv",
                "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
                "path": "/01-bronze/esg/xyz_company.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/xyz_company.csv",
                "replicatedFrom": null,
                "replicatedTo": null,
                "size": 2813,
                "userProperties": null
            },
            "classifications": [
                {
                    "entityGuid": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "source": "LabelService",
                    "typeName": "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
                },
                {
                    "attributes": {
                        "confidence": null
                    },
                    "entityGuid": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
                }
            ],
            "collectionId": "esg-26fa7f24-pv",
            "createTime": 1645631429711,
            "createdBy": "ServiceAdmin",
            "guid": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
            "lastModifiedTS": "14",
            "relationshipAttributes": {
                "attachedSchema": [],
                "inputToProcesses": [],
                "meanings": [],
                "outputFromProcesses": [],
                "schema": [],
                "tabular_schema": {
                    "displayText": "tabular_schema",
                    "entityStatus": "ACTIVE",
                    "guid": "1025260d-b33e-4e8a-9f2c-12f6f6f60000",
                    "relationshipAttributes": {
                        "typeName": "tabular_schema_datasets"
                    },
                    "relationshipGuid": "ca638a66-da4e-4f24-8407-58c79753f04c",
                    "relationshipStatus": "ACTIVE",
                    "relationshipType": "tabular_schema_datasets",
                    "typeName": "tabular_schema"
                }
            },
            "sourceDetails": {
                "ScanLastModifiedAt": "2022-02-23T15:45:56.3612911Z",
                "ScanResourceId": "datasources/AzureDataLakeStorage-Gbm/scans/Scan-Xei",
                "ScanRuleSetLastModifiedAt": "2021-12-09T18:06:33.0707225Z",
                "ScanRuleSetResourceId": "scanrulesets/AdlsGen2"
            },
            "status": "ACTIVE",
            "typeName": "azure_datalake_gen2_path",
            "updateTime": 1646040314960,
            "updatedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
            "version": 0
        },
        {
            "attributes": {
                "ACL": null,
                "contentType": "application/octet-stream",
                "description": "This is a long description.",
                "groups": null,
                "isFile": true,
                "modifiedTime": 0,
                "name": "filename.csv",
                "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
                "path": "/01-bronze/esg/filename.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/filename.csv",
                "replicatedFrom": null,
                "replicatedTo": null,
                "size": 2826,
                "userProperties": null
            },
            "createTime": 1646062630127,
            "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
            "guid": "a2f6b9e9-483c-439a-b169-59241502a97a",
            "lastModifiedTS": "7",
            "relationshipAttributes": {
                "attachedSchema": [],
                "inputToProcesses": [],
                "meanings": [],
                "outputFromProcesses": [],
                "schema": []
            },
            "sourceDetails": {
                "userModifiedAttributes": [
                    "owner",
                    "size",
                    "isFile",
                    "description",
                    "contentType"
                ]
            },
            "status": "ACTIVE",
            "typeName": "azure_datalake_gen2_path",
            "updateTime": 1646062868348,
            "updatedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
            "version": 0
        }
    ],
    "referredEntities": {}
}
```
</p>
</details>
