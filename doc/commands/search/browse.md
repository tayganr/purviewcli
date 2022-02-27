# pv search browse
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > browse

## Description
Browse entities by path or entity type.

## Syntax
```
pv search browse (--entityType=<val> | --path=<val>) [--limit=<val> --offset=<val>]
```

## Required Arguments
`--entityType` (string)  
The entity type to browse as the root level entry point.

`--path` (string)  
The path to browse the next level child entities.

## Optional Arguments
`--limit` (integer)  
The number of browse items we hope to return. The maximum value is 10000.

`--offset` (integer)  
The offset. The default value is 0. The maximum value is 100000.

## API Mapping
Catalog Data Plane > Discovery > [Browse](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/browse)
```
POST https://{accountName}.purview.azure.com/catalog/api/browse
```

## Examples
Browse entities by entity type.
```powershell
pv search browse --entityType "azure_datalake_gen2_path"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "@search.count": 4,
    "value": [
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "isLeaf": true,
            "name": "abc_company.csv",
            "owner": [
                {
                    "contactType": "Expert",
                    "displayName": "Person1 Name",
                    "id": "a1f659ac-be30-4292-bda0-17965b28324e",
                    "mail": "email1@microsoft.com"
                },
                {
                    "contactType": "Owner",
                    "displayName": "Person2 Name",
                    "id": "095354ff-cae8-44ff-8120-22ec5a941b40",
                    "mail": "email2@microsoft.com"
                }
            ],
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg/abc_company.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/abc_company.csv"
        },
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "6374e9e8-4719-4747-b2d2-054548023ae2",
            "isLeaf": true,
            "name": "def_company.csv",
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg/def_company.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/def_company.csv"
        },
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "d20f67cf-139e-4063-b751-ce56c3035492",
            "isLeaf": false,
            "name": "esg",
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/"
        },
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
            "isLeaf": true,
            "name": "xyz_company.csv",
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg/xyz_company.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/xyz_company.csv"
        }
    ]
}
```
</p>
</details><br />

Browse entities by path.
```powershell
pv search browse --path "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "@search.count": 3,
    "value": [
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "isLeaf": true,
            "name": "abc_company.csv",
            "owner": [
                {
                    "contactType": "Expert",
                    "displayName": "Person1 Name",
                    "id": "a1f659ac-be30-4292-bda0-17965b28324e",
                    "mail": "email2@microsoft.com"
                },
                {
                    "contactType": "Owner",
                    "displayName": "Person2 Name",
                    "id": "095354ff-cae8-44ff-8120-22ec5a941b40",
                    "mail": "email1@microsoft.com"
                }
            ],
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg/abc_company.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/abc_company.csv"
        },
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "6374e9e8-4719-4747-b2d2-054548023ae2",
            "isLeaf": true,
            "name": "def_company.csv",
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg/def_company.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/def_company.csv"
        },
        {
            "entityType": "azure_datalake_gen2_path",
            "id": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
            "isLeaf": true,
            "name": "xyz_company.csv",
            "path": "/azure_storage_account#esg26fa7f24adls.core.windows.net/azure_datalake_gen2_service#esg26fa7f24adls.dfs.core.windows.net/azure_datalake_gen2_filesystem#01-bronze/azure_datalake_gen2_path#esg/xyz_company.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/xyz_company.csv"
        }
    ]
}
```
</p>
</details>