# pv entity readUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readUniqueAttribute

## Description
Get complete definition of an entity given its type and unique attribute. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:<attrName>=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

## Syntax
```
pv entity readUniqueAttribute --typeName=<val> --qualifiedName=<val> [--ignoreRelationships --minExtInfo]
```

## Required Arguments
`--typeName` (string)  
The name of the type.

`--qualifiedName` (string)  
The qualified name of the entity.

## Optional Arguments
`--ignoreRelationships` (boolean)  
Whether to ignore relationship attributes.

`--minExtInfo` (boolean)  
Whether to return minimal information for referred entities.

## API Mapping
Catalog Data Plane > Entity > [Get By Unique Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-by-unique-attributes)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}
```

## Examples
Get an entity definition by specifying the entities type name and qualified name.
```powershell
pv entity readUniqueAttribute --typeName "azure_datalake_gen2_path" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/xyz_company.csv"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "entity": {
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
    "referredEntities": {}
}
```
</p>
</details>
