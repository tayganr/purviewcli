# pv entity read
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > read

## Description
Get complete definition of an entity given its GUID.

## Syntax
```
pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
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
Catalog Data Plane > Entity > [Get By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}
```

## Examples
Get the complete definition of an existing entity via the entities GUID.
```powershell
pv entity read --guid "c6a7811a-0699-44d0-b0be-68babe560ab2"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "entity": {
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
    "referredEntities": {}
}
```
</p>
</details><br />

Get the complete definition of an existing entity via the entities GUID (ignoring relationships).
```powershell
pv entity read --guid "c6a7811a-0699-44d0-b0be-68babe560ab2" --ignoreRelationships
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "entity": {
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
