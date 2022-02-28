# pv entity readBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readBulk

## Description
List entities in bulk identified by its GUIDs.

## Syntax
```
pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

## Optional Arguments
`--ignoreRelationships` (boolean)  
Whether to ignore relationship attributes.

`--minExtInfo` (boolean)  
Whether to return minimal information for referred entities.

## API Mapping
Catalog Data Plane > Entity > [List By Guids](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/list-by-guids)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk
```

## Examples
Get the complete definition for a list of existing entities (bulk) via their GUID.
```powershell
pv entity readBulk --guid "c6a7811a-0699-44d0-b0be-68babe560ab2" --guid "6374e9e8-4719-4747-b2d2-054548023ae2" --guid "dcd41879-dda2-4b3c-8c97-9b76d39799b1"
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
                "description": "Portfolio company data collection template - Company ABC.",
                "groups": "$superuser",
                "isFile": true,
                "modifiedTime": 1645630373000,
                "name": "abc_company.csv",
                "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
                "path": "/01-bronze/esg/abc_company.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/abc_company.csv",
                "replicatedFrom": null,
                "replicatedTo": null,
                "size": 2826,
                "userProperties": null
            },
            "classifications": [
                {
                    "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "source": "LabelService",
                    "typeName": "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
                },
                {
                    "attributes": {
                        "confidence": null
                    },
                    "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "typeName": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER"
                },
                {
                    "attributes": {
                        "confidence": null
                    },
                    "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "typeName": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER"
                },
                {
                    "attributes": {
                        "certifiedBy": "Taygan Rifat",
                        "endorsement": "Certified"
                    },
                    "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "2",
                    "typeName": "MICROSOFT.POWERBI.ENDORSEMENT"
                },
                {
                    "attributes": {
                        "confidence": null
                    },
                    "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
                }
            ],
            "collectionId": "esg-26fa7f24-pv",
            "contacts": {
                "Expert": [
                    {
                        "id": "a1f659ac-be30-4292-bda0-17965b28324e"
                    }
                ],
                "Owner": [
                    {
                        "id": "095354ff-cae8-44ff-8120-22ec5a941b40"
                    }
                ]
            },
            "createTime": 1645631429587,
            "createdBy": "ServiceAdmin",
            "guid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "lastModifiedTS": "9",
            "relationshipAttributes": {
                "attachedSchema": [],
                "inputToProcesses": [],
                "meanings": [
                    {
                        "displayText": "Diversity of board members",
                        "entityStatus": "ACTIVE",
                        "guid": "f1496766-3af2-461a-8d59-6eca8a716887",
                        "relationshipAttributes": {
                            "attributes": {
                                "confidence": null,
                                "createdBy": null,
                                "description": null,
                                "expression": null,
                                "source": null,
                                "status": null,
                                "steward": null
                            },
                            "typeName": "AtlasGlossarySemanticAssignment"
                        },
                        "relationshipGuid": "28013ca5-56b0-45a6-94da-7ffab0e173d6",
                        "relationshipStatus": "ACTIVE",
                        "relationshipType": "AtlasGlossarySemanticAssignment",
                        "typeName": "AtlasGlossaryTerm"
                    },
                    {
                        "displayText": "Work related injuries",
                        "entityStatus": "ACTIVE",
                        "guid": "74a7901e-7049-4858-a103-4ffb889b5fc9",
                        "relationshipAttributes": {
                            "attributes": {
                                "confidence": null,
                                "createdBy": null,
                                "description": null,
                                "expression": null,
                                "source": null,
                                "status": null,
                                "steward": null
                            },
                            "typeName": "AtlasGlossarySemanticAssignment"
                        },
                        "relationshipGuid": "d3f6fc76-c40b-4740-9cfa-c0eab6c277ae",
                        "relationshipStatus": "ACTIVE",
                        "relationshipType": "AtlasGlossarySemanticAssignment",
                        "typeName": "AtlasGlossaryTerm"
                    },
                    {
                        "displayText": "Employee feedback / survey",
                        "entityStatus": "ACTIVE",
                        "guid": "5e492945-85a5-42c4-bbcd-dbfdb2dd8713",
                        "relationshipAttributes": {
                            "attributes": {
                                "confidence": null,
                                "createdBy": null,
                                "description": null,
                                "expression": null,
                                "source": null,
                                "status": null,
                                "steward": null
                            },
                            "typeName": "AtlasGlossarySemanticAssignment"
                        },
                        "relationshipGuid": "777f339a-1122-41eb-84be-ab03eefc4d2f",
                        "relationshipStatus": "ACTIVE",
                        "relationshipType": "AtlasGlossarySemanticAssignment",
                        "typeName": "AtlasGlossaryTerm"
                    }
                ],
                "outputFromProcesses": [],
                "schema": [],
                "tabular_schema": {
                    "displayText": "tabular_schema",
                    "entityStatus": "ACTIVE",
                    "guid": "85f0ef7f-b9ad-4f0e-bf2c-15f6f6f60000",
                    "relationshipAttributes": {
                        "typeName": "tabular_schema_datasets"
                    },
                    "relationshipGuid": "116b6a1f-1a7d-4848-88ee-e1bb0fdea3aa",
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
                "description": null,
                "groups": "$superuser",
                "isFile": true,
                "modifiedTime": 1645631075000,
                "name": "def_company.csv",
                "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
                "path": "/01-bronze/esg/def_company.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/def_company.csv",
                "replicatedFrom": null,
                "replicatedTo": null,
                "size": 2813,
                "userProperties": null
            },
            "classifications": [
                {
                    "entityGuid": "6374e9e8-4719-4747-b2d2-054548023ae2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "source": "LabelService",
                    "typeName": "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
                },
                {
                    "attributes": {
                        "confidence": null
                    },
                    "entityGuid": "6374e9e8-4719-4747-b2d2-054548023ae2",
                    "entityStatus": "ACTIVE",
                    "lastModifiedTS": "1",
                    "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
                }
            ],
            "collectionId": "esg-26fa7f24-pv",
            "createTime": 1645631429587,
            "createdBy": "ServiceAdmin",
            "guid": "6374e9e8-4719-4747-b2d2-054548023ae2",
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
                    "guid": "b730d156-6efa-4e17-80ef-56f6f6f60000",
                    "relationshipAttributes": {
                        "typeName": "tabular_schema_datasets"
                    },
                    "relationshipGuid": "798fccaa-7309-4f10-87e7-eb49a0067efb",
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
        }
    ],
    "referredEntities": {}
}
```
</p>
</details>