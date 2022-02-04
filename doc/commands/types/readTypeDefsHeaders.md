# pv types readTypeDefsHeaders
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTypeDefsHeaders

## Description
List all type definitions returned as a list of minimal information header.

## Syntax
```
pv types readTypeDefsHeaders [--includeTermTemplate --type=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--includeTermTemplate` (boolean)  
Whether to include termtemplatedef when returning all typedefs. Default: false.

`--type` (string)  
Restrict results to a specific type of type definition (classification | entity | enum | relationship | struct | term_template).

## API Mapping
Catalog Data Plane > Types > [List Type Definition Headers](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/list-type-definition-headers)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs/headers
```

## Examples
Get all type definition headers.
```powershell
pv types readTypeDefsHeaders
```

Get all type definition headers for a particular type.
```powershell
pv types readTypeDefsHeaders --type "struct"
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "category": "STRUCT",
        "guid": "9e2e9898-17e9-b378-47f9-c946b45bb595",
        "name": "blob_soft_deleted_state",
        "serviceType": "Azure Blob Storage"
    },
    {
        "category": "STRUCT",
        "guid": "e48b74f3-9df8-5d16-2a96-5814a112d91c",
        "name": "aws_tag",
        "serviceType": "aws"
    },
    {
        "category": "STRUCT",
        "guid": "c46b9bfe-aa33-bd98-1ab1-12534b4a4308",
        "name": "aws_cloud_watch_metric",
        "serviceType": "aws"
    },
    {
        "category": "STRUCT",
        "guid": "7eca7b30-b5a5-da54-bcc0-83e4fea11046",
        "name": "aws_s3_access_policy",
        "serviceType": "aws"
    },
    {
        "category": "STRUCT",
        "guid": "8c02797d-fa17-857e-329f-8d47b5270fe8",
        "name": "aws_s3_bucket_lifeCycleRule",
        "serviceType": "aws"
    },
    {
        "category": "STRUCT",
        "guid": "d5e52013-f7a4-db1b-682c-08a7a07f0ffe",
        "name": "cosmosdb_timetolive",
        "serviceType": "Azure Cosmos DB"
    },
    {
        "category": "STRUCT",
        "guid": "fd5e2b6a-6b2f-db01-ae48-0ad67f1efc6e",
        "name": "hive_serde",
        "serviceType": "hive"
    },
    {
        "category": "STRUCT",
        "guid": "f4318336-471c-e256-08f3-0c320b1a3eef",
        "name": "hive_order",
        "serviceType": "hive"
    },
    {
        "category": "STRUCT",
        "guid": "f5e943b6-09dd-d672-a3a5-296546c5c163",
        "name": "fs_permissions",
        "serviceType": "file_system"
    },
    {
        "category": "STRUCT",
        "guid": "d96ff541-abd9-a199-58b6-2deb81e4ca5f",
        "name": "cosmosdb_offer",
        "serviceType": "Azure Cosmos DB"
    },
    {
        "category": "STRUCT",
        "guid": "fcd2963f-b042-e896-53d9-b310c33fd0a1",
        "name": "blob_delete_retention_policy",
        "serviceType": "Azure Blob Storage"
    }
]
```
</p>
</details>