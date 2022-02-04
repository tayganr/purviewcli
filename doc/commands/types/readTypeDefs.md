# pv types readTypeDefs
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTypeDefs

## Description
Get all type definitions in Atlas in bulk.

## Syntax
```
pv types readTypeDefs [--includeTermTemplate --type=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--includeTermTemplate` (boolean)  
Whether to include termtemplatedef when returning all typedefs. Default: false.

`--type` (string)  
Restrict results to a specific type of type definition (classification | entity | enum | relationship | struct | term_template).

## API Mapping
Catalog Data Plane > Types > [Get All Type Definitions](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-all-type-definitions)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

## Examples
Get all type definitions for a particular type.
```powershell
pv types readTypeDefs --type "enum"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "classificationDefs": [],
    "entityDefs": [],
    "enumDefs": [
        {
            "category": "ENUM",
            "createTime": 1615787943686,
            "createdBy": "admin",
            "description": "glossary_term_status_value",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Approved"
                },
                {
                    "ordinal": 1,
                    "value": "Alert"
                },
                {
                    "ordinal": 2,
                    "value": "Expired"
                },
                {
                    "ordinal": 3,
                    "value": "Draft"
                }
            ],
            "guid": "6e30d01e-f5d0-9799-08e7-09b4f276c09c",
            "lastModifiedTS": "1",
            "name": "glossary_term_status_value",
            "typeVersion": "1.0",
            "updateTime": 1615787943686,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787943608,
            "createdBy": "admin",
            "description": "TermRelationshipStatus defines how reliable the relationship is between two glossary terms",
            "elementDefs": [
                {
                    "description": "DRAFT means the relationship is under development.",
                    "ordinal": 0,
                    "value": "DRAFT"
                },
                {
                    "description": "ACTIVE means the relationship is validated and in use.",
                    "ordinal": 1,
                    "value": "ACTIVE"
                },
                {
                    "description": "DEPRECATED means the the relationship is being phased out.",
                    "ordinal": 2,
                    "value": "DEPRECATED"
                },
                {
                    "description": "OBSOLETE means that the relationship should not be used anymore.",
                    "ordinal": 3,
                    "value": "OBSOLETE"
                },
                {
                    "description": "OTHER means that there is another status.",
                    "ordinal": 99,
                    "value": "OTHER"
                }
            ],
            "guid": "42185ddb-29be-e911-ea52-890154eb07c0",
            "lastModifiedTS": "2",
            "name": "AtlasGlossaryTermRelationshipStatus",
            "serviceType": "atlas_core",
            "typeVersion": "1.1",
            "updateTime": 1615787943973,
            "updatedBy": "admin",
            "version": 2
        },
        {
            "category": "ENUM",
            "createTime": 1615787945788,
            "createdBy": "admin",
            "description": "storage_account_sku",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Standard_LRS"
                },
                {
                    "ordinal": 1,
                    "value": "Standard_GRS"
                },
                {
                    "ordinal": 2,
                    "value": "Standard_RAGRS"
                },
                {
                    "ordinal": 3,
                    "value": "Standard_ZRS"
                },
                {
                    "ordinal": 4,
                    "value": "Premium_LRS"
                }
            ],
            "guid": "fc65fc32-3596-56ea-f430-99f0cb71debd",
            "lastModifiedTS": "1",
            "name": "storage_account_sku",
            "typeVersion": "1.0",
            "updateTime": 1615787945788,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787945788,
            "createdBy": "admin",
            "description": "blob_access_tier",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Unknown"
                },
                {
                    "ordinal": 1,
                    "value": "Hot"
                },
                {
                    "ordinal": 2,
                    "value": "Cool"
                },
                {
                    "ordinal": 3,
                    "value": "Archive"
                }
            ],
            "guid": "edce5d5f-699b-f36f-e4d8-8e18bb4b10f5",
            "lastModifiedTS": "1",
            "name": "blob_access_tier",
            "serviceType": "Azure Blob Storage",
            "typeVersion": "1.0",
            "updateTime": 1615787945788,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787946620,
            "createdBy": "admin",
            "description": "ads_snapshot_status",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Succeeded"
                },
                {
                    "ordinal": 1,
                    "value": "Failed"
                },
                {
                    "ordinal": 1,
                    "value": "Cancelled"
                }
            ],
            "guid": "ef90949b-3711-9a46-ba1e-5137abfe2b26",
            "lastModifiedTS": "1",
            "name": "ads_snapshot_status",
            "typeVersion": "1.0",
            "updateTime": 1615787946620,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787945788,
            "createdBy": "admin",
            "description": "container_public_access_level",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Off"
                },
                {
                    "ordinal": 1,
                    "value": "Container"
                },
                {
                    "ordinal": 2,
                    "value": "Blob"
                },
                {
                    "ordinal": 3,
                    "value": "Unknown"
                }
            ],
            "guid": "eb9f089d-d8b1-068d-bfbf-84bd267f5904",
            "lastModifiedTS": "1",
            "name": "container_public_access_level",
            "serviceType": "Azure Blob Storage",
            "typeVersion": "1.0",
            "updateTime": 1615787945788,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787944125,
            "createdBy": "admin",
            "description": "file_action",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "NONE"
                },
                {
                    "ordinal": 1,
                    "value": "EXECUTE"
                },
                {
                    "ordinal": 2,
                    "value": "WRITE"
                },
                {
                    "ordinal": 3,
                    "value": "WRITE_EXECUTE"
                },
                {
                    "ordinal": 4,
                    "value": "READ"
                },
                {
                    "ordinal": 5,
                    "value": "READ_EXECUTE"
                },
                {
                    "ordinal": 6,
                    "value": "READ_WRITE"
                },
                {
                    "ordinal": 7,
                    "value": "ALL"
                }
            ],
            "guid": "a8681e87-f59c-78e0-7fc1-9c0bcc4553f7",
            "lastModifiedTS": "2",
            "name": "file_action",
            "serviceType": "file_system",
            "typeVersion": "1.1",
            "updateTime": 1615787944505,
            "updatedBy": "admin",
            "version": 2
        },
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
        },
        {
            "category": "ENUM",
            "createTime": 1615787945788,
            "createdBy": "admin",
            "description": "storage_account_kind",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "StorageClassic"
                },
                {
                    "ordinal": 1,
                    "value": "StorageV2"
                },
                {
                    "ordinal": 2,
                    "value": "BlobStorage"
                }
            ],
            "guid": "ad3d7a83-08c3-9717-1305-e18408e10308",
            "lastModifiedTS": "1",
            "name": "storage_account_kind",
            "typeVersion": "1.0",
            "updateTime": 1615787945788,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787943608,
            "createdBy": "admin",
            "description": "TermAssignmentStatus defines how much the semantic assignment should be trusted.",
            "elementDefs": [
                {
                    "description": "DISCOVERED means that the semantic assignment was added by a discovery engine.",
                    "ordinal": 0,
                    "value": "DISCOVERED"
                },
                {
                    "description": "PROPOSED means that the semantic assignment was proposed by person - they may be a subject matter expert, or consumer of the Referenceable asset",
                    "ordinal": 1,
                    "value": "PROPOSED"
                },
                {
                    "description": "IMPORTED means that the semantic assignment has been imported from outside of the open metadata cluster",
                    "ordinal": 2,
                    "value": "IMPORTED"
                },
                {
                    "description": "VALIDATED means that the semantic assignment has been reviewed and is highly trusted.",
                    "ordinal": 3,
                    "value": "VALIDATED"
                },
                {
                    "description": "DEPRECATED means that the semantic assignment is being phased out. There may be another semantic assignment to the Referenceable that will ultimately replace this one.",
                    "ordinal": 4,
                    "value": "DEPRECATED"
                },
                {
                    "description": "OBSOLETE means that the semantic assignment is no longer in use,",
                    "ordinal": 5,
                    "value": "OBSOLETE"
                },
                {
                    "description": "OTHER means that the semantic assignment value does not match any of the other Term Assignment Status values",
                    "ordinal": 6,
                    "value": "OTHER"
                }
            ],
            "guid": "b9aaf55f-2689-8680-cad4-7bea87aa51f2",
            "lastModifiedTS": "2",
            "name": "AtlasGlossaryTermAssignmentStatus",
            "serviceType": "atlas_core",
            "typeVersion": "1.1",
            "updateTime": 1615787943973,
            "updatedBy": "admin",
            "version": 2
        },
        {
            "category": "ENUM",
            "createTime": 1615787946118,
            "createdBy": "admin",
            "description": "cosmosdb_account_api",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "SQL"
                },
                {
                    "ordinal": 1,
                    "value": "MongoDb"
                },
                {
                    "ordinal": 2,
                    "value": "Cassandra"
                },
                {
                    "ordinal": 3,
                    "value": "Table"
                },
                {
                    "ordinal": 4,
                    "value": "Gremlin"
                }
            ],
            "guid": "494eb577-0c4e-b781-4c8e-e6a7e3b5f404",
            "lastModifiedTS": "1",
            "name": "cosmosdb_account_api",
            "serviceType": "Azure Cosmos DB",
            "typeVersion": "1.0",
            "updateTime": 1615787946118,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787944156,
            "createdBy": "admin",
            "description": "hive_principal_type",
            "elementDefs": [
                {
                    "ordinal": 1,
                    "value": "USER"
                },
                {
                    "ordinal": 2,
                    "value": "ROLE"
                },
                {
                    "ordinal": 3,
                    "value": "GROUP"
                }
            ],
            "guid": "bb326328-3a0c-46f6-8d43-2d96abc35cc4",
            "lastModifiedTS": "2",
            "name": "hive_principal_type",
            "serviceType": "hive",
            "typeVersion": "1.1",
            "updateTime": 1615787944573,
            "updatedBy": "admin",
            "version": 2
        },
        {
            "category": "ENUM",
            "createTime": 1615787946620,
            "createdBy": "admin",
            "description": "ads_share_type",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Snapshot"
                },
                {
                    "ordinal": 1,
                    "value": "InPlace"
                }
            ],
            "guid": "24fafa85-6344-c42c-ea38-1db696e65123",
            "lastModifiedTS": "1",
            "name": "ads_share_type",
            "typeVersion": "1.0",
            "updateTime": 1615787946620,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787946620,
            "createdBy": "admin",
            "description": "ads_snapshot_type",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Incremental"
                },
                {
                    "ordinal": 1,
                    "value": "FullCopy"
                }
            ],
            "guid": "f3a24724-e47f-7f77-339b-67153b6274bf",
            "lastModifiedTS": "1",
            "name": "ads_snapshot_type",
            "typeVersion": "1.0",
            "updateTime": 1615787946620,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787948145,
            "createdBy": "admin",
            "description": "powerbi_endorsement_status",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "Promoted"
                },
                {
                    "ordinal": 1,
                    "value": "Certified"
                }
            ],
            "guid": "32f31348-5c77-5e27-1198-19c2cfc24499",
            "lastModifiedTS": "1",
            "name": "powerbi_endorsement_status",
            "serviceType": "Power BI",
            "typeVersion": "1.0",
            "updateTime": 1615787948145,
            "updatedBy": "admin",
            "version": 1
        },
        {
            "category": "ENUM",
            "createTime": 1615787948493,
            "createdBy": "admin",
            "description": "parquet_field_repetition_type",
            "elementDefs": [
                {
                    "ordinal": 0,
                    "value": "optional"
                },
                {
                    "ordinal": 1,
                    "value": "required"
                },
                {
                    "ordinal": 2,
                    "value": "repeated"
                }
            ],
            "guid": "d100c837-68c7-283a-764e-ea86be31c0b4",
            "lastModifiedTS": "1",
            "name": "parquet_field_repetition_type",
            "typeVersion": "1.0",
            "updateTime": 1615787948493,
            "updatedBy": "admin",
            "version": 1
        }
    ],
    "relationshipDefs": [],
    "structDefs": []
}
```
</p>
</details>

Get all type definitions (not including term templates).
```powershell
pv types readTypeDefs
```

Get all type definitions (including term templates).
```powershell
pv types readTypeDefs --includeTermTemplate
```