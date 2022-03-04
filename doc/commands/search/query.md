# pv search query
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > query

## Description
Gets data using search.

## Syntax
```
pv search query [--keywords=<val> --limit=<val> --offset=<val> --filterFile=<val> --facets-file=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all searchable fields.

`--limit` (integer)  
The limit of the number of the search result. default value is 50; maximum value is 1000.

`--offset` (integer)  
The offset. The default value is 0. The maximum value is 100000.

`--filterFile` (string)  
The filter for the search.

`--facets-file` (string)  
The content of a search facet result item.

## API Mapping
Catalog Data Plane > Discovery > [Query](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/query)
```
POST https://{accountName}.purview.azure.com/catalog/api/search/query
```

## Examples
Search without specifying a keyword.
```powershell
pv search query
```

Search by keyword.
```powershell
pv search query --keywords "ESG"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "@search.count": 17,
    "@search.facets": null,
    "value": [
        {
            "@search.highlights": {
                "qualifiedName": [
                    "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/<em>esg</em>/abc_company.csv"
                ]
            },
            "@search.score": 1120.8326,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [
                "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
                "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER",
                "MICROSOFT.POWERBI.ENDORSEMENT"
            ],
            "collectionId": "esg-26fa7f24-pv",
            "contact": [
                {
                    "contactType": "Expert",
                    "id": "a1f659ac-be30-4292-bda0-17965b28324e"
                },
                {
                    "contactType": "Owner",
                    "id": "095354ff-cae8-44ff-8120-22ec5a941b40"
                }
            ],
            "description": "Portfolio company data collection template - Company ABC.",
            "entityType": "azure_datalake_gen2_path",
            "id": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "label": [
                "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
            ],
            "name": "abc_company.csv",
            "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/abc_company.csv",
            "term": [
                {
                    "glossaryName": "Glossary",
                    "guid": "5e492945-85a5-42c4-bbcd-dbfdb2dd8713",
                    "name": "Employee feedback / survey"
                },
                {
                    "glossaryName": "Glossary",
                    "guid": "74a7901e-7049-4858-a103-4ffb889b5fc9",
                    "name": "Work related injuries"
                },
                {
                    "glossaryName": "Glossary",
                    "guid": "f1496766-3af2-461a-8d59-6eca8a716887",
                    "name": "Diversity of board members"
                }
            ]
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/<em>esg</em>/def_company.csv"
                ]
            },
            "@search.score": 975.9448,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_path",
            "id": "6374e9e8-4719-4747-b2d2-054548023ae2",
            "label": [
                "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
            ],
            "name": "def_company.csv",
            "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/def_company.csv",
            "term": [
                {
                    "glossaryName": "Glossary",
                    "guid": "7323f934-48f2-4881-909c-723d7d28c5d7",
                    "name": "Days lost due to injury"
                }
            ]
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/<em>esg</em>/xyz_company.csv"
                ]
            },
            "@search.score": 944.66376,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_path",
            "id": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
            "label": [
                "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
            ],
            "name": "xyz_company.csv",
            "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/xyz_company.csv",
            "term": []
        },
        {
            "@search.highlights": {
                "name": [
                    "<em>esg</em>"
                ],
                "qualifiedName": [
                    "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/<em>esg</em>/"
                ]
            },
            "@search.score": 107.570625,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_path",
            "id": "d20f67cf-139e-4063-b751-ce56c3035492",
            "label": [],
            "name": "esg",
            "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/",
            "term": []
        },
        {
            "@search.highlights": {
                "name": [
                    "<em>esg</em>-26fa7f24-ds"
                ],
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/<em>esg</em>/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds"
                ]
            },
            "@search.score": 71.166306,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_account",
            "id": "621da392-5012-483a-b24f-17bf93d51f18",
            "label": [],
            "name": "esg-26fa7f24-ds",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds",
            "term": []
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/<em>esg</em>/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds/shareSubscriptions/share_company_abc"
                ]
            },
            "@search.score": 69.83491,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_share_subscription",
            "id": "04ab2c93-78fa-4f23-953a-4d1286930520",
            "label": [],
            "name": "share_company_abc",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_abc",
            "term": []
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/<em>esg</em>/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds/shareSubscriptions/share_company_def"
                ]
            },
            "@search.score": 69.83491,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_share_subscription",
            "id": "88bd838b-41a4-4644-afe8-e2fbdfc60441",
            "label": [],
            "name": "share_company_def",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_def",
            "term": []
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/<em>esg</em>/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds/shareSubscriptions/share_company_xyz"
                ]
            },
            "@search.score": 69.83491,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_share_subscription",
            "id": "b8720d56-e05b-47e5-bd6c-4d96f5f488ad",
            "label": [],
            "name": "share_company_xyz",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_xyz",
            "term": []
        },
        {
            "@search.highlights": {
                "name": [
                    "<em>esg</em>26fa7f24adls"
                ]
            },
            "@search.score": 58.674232,
            "assetType": [
                "Azure Blob Storage",
                "Azure Files",
                "Azure Table Storage",
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_storage_account",
            "id": "0f354421-2284-458f-b99c-0030a73c2dca",
            "label": [],
            "name": "esg26fa7f24adls",
            "owner": null,
            "qualifiedName": "https://esg26fa7f24adls.core.windows.net",
            "term": []
        },
        {
            "@search.highlights": {
                "name": [
                    "<em>esg</em>26fa7f24adls"
                ]
            },
            "@search.score": 58.674232,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_service",
            "id": "79f230dc-2450-442a-b574-d8969ab23dbc",
            "label": [],
            "name": "esg26fa7f24adls",
            "owner": null,
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net",
            "term": []
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg_company_01/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds/shareSubscriptions/share_company_abc/snapshots/cf826bf5-3dea-42d1-99c2-87cfc7726779"
                ]
            },
            "@search.score": 27.704351,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_received_snapshot",
            "id": "ef204f7b-1c1c-4d6c-b365-e01505732459",
            "label": [],
            "name": "share_company_abc",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg_company_01/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_abc/snapshots/cf826bf5-3dea-42d1-99c2-87cfc7726779",
            "term": []
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg_company_03/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds/shareSubscriptions/share_company_def/snapshots/9abd57ca-a744-4c96-acdb-5972024f0daf"
                ]
            },
            "@search.score": 27.704351,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_received_snapshot",
            "id": "48962df1-534d-4151-9e93-7369f33e550e",
            "label": [],
            "name": "share_company_def",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg_company_03/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_def/snapshots/9abd57ca-a744-4c96-acdb-5972024f0daf",
            "term": []
        },
        {
            "@search.highlights": {
                "qualifiedName": [
                    "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg_company_02/providers/Microsoft.DataShare/accounts/<em>esg</em>-26fa7f24-ds/shareSubscriptions/share_company_xyz/snapshots/0dfd8ea7-31a2-4f85-8bc3-d116fda422b1"
                ]
            },
            "@search.score": 27.704351,
            "assetType": [
                "Azure Data Share"
            ],
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "ads_received_snapshot",
            "id": "ddab9962-e778-4e46-9755-6e4096fb7889",
            "label": [],
            "name": "share_company_xyz",
            "owner": null,
            "qualifiedName": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/esg_company_02/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_xyz/snapshots/0dfd8ea7-31a2-4f85-8bc3-d116fda422b1",
            "term": []
        },
        {
            "@search.highlights": {
                "name": [
                    "<em>esg</em>26fa7f24fs"
                ]
            },
            "@search.score": 14.065545,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_filesystem",
            "id": "f2359056-7bb8-4b3c-a866-367fd4c254a7",
            "label": [],
            "name": "esg26fa7f24fs",
            "owner": null,
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/esg26fa7f24fs",
            "term": []
        },
        {
            "@search.highlights": null,
            "@search.score": 10.993714,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_filesystem",
            "id": "04f2bb30-91db-404b-a8e1-d65e45338929",
            "label": [],
            "name": "01-bronze",
            "owner": null,
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze",
            "term": []
        },
        {
            "@search.highlights": null,
            "@search.score": 10.993714,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_filesystem",
            "id": "bbb9ff1d-f880-435e-ac87-d6fd5676d8f0",
            "label": [],
            "name": "02-silver",
            "owner": null,
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/02-silver",
            "term": []
        },
        {
            "@search.highlights": null,
            "@search.score": 10.993714,
            "assetType": [
                "Azure Data Lake Storage Gen2"
            ],
            "classification": [],
            "collectionId": "esg-26fa7f24-pv",
            "description": null,
            "entityType": "azure_datalake_gen2_filesystem",
            "id": "d1df0e2d-18b1-42ff-ab52-d7c954affa1a",
            "label": [],
            "name": "03-gold",
            "owner": null,
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/03-gold",
            "term": []
        }
    ]
}
```
</p>
</details>