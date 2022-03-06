# pv insight filesWithoutResourceSet
[Command Reference](../../../README.md#command-reference) > [insight](./main.md) > filesWithoutResourceSet

## Description
Number of files not stored in a resource set by sourceType.

## Syntax
```
pv insight filesWithoutResourceSet
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
```
GET https://{accountName}.purview.azure.com/mapanddiscover/reports/serverless/asset2/filesWithoutResourceSet/getSnapshot
```

## Examples
Get number of fiels not stored in a resource set.
```powershell
pv insight filesWithoutResourceSet
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "records": [
        {
            "count": 10,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-combo/2021/",
            "resourceSetCount": 0,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 9,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-combo/2020/",
            "resourceSetCount": 0,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 5,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "resourceSetCount": 0,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 3,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/",
            "resourceSetCount": 0,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 2,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "resourceSetCount": 0,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 65,
            "resourceSetCount": 27,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 12,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles6/",
            "resourceSetCount": 21,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 6,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles3/",
            "resourceSetCount": 0,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 6,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "resourceSetCount": 0,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 6,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles/",
            "resourceSetCount": 0,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 3,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles9/",
            "resourceSetCount": 0,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 40,
            "resourceSetCount": 63,
            "sourceType": "Azure Data Lake Storage Gen2"
        }
    ],
    "snapshotTime": "2021-11-23T13:24:03Z"
}
```
</p>
</details>
