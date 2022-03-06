# pv insight filesAggregation
[Command Reference](../../../README.md#command-reference) > [insight](./main.md) > filesAggregation

## Description
File count and size by fileType and sourceType.

## Syntax
```
pv insight filesAggregation
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
```
GET https://{accountName}.purview.azure.com/mapanddiscover/reports/serverless/asset2/filesAggregation/getSnapshot
```

## Examples
Get file statistics by fileType and sourceType.
```powershell
pv insight filesAggregation
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "records": [
        {
            "currBytes": 763118,
            "currCount": 9,
            "fileType": "csv",
            "prev30dBytes": 7417,
            "prev30dCount": 1,
            "prev7dBytes": 763118,
            "prev7dCount": 9,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 4495942642,
            "currCount": 63,
            "fileType": "txt",
            "prev30dBytes": 122,
            "prev30dCount": 1,
            "prev7dBytes": 4495942642,
            "prev7dCount": 63,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 166707599,
            "currCount": 34,
            "fileType": "pdf",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 166707599,
            "prev7dCount": 34
        },
        {
            "currBytes": 31291308,
            "currCount": 5,
            "fileType": "pdf",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 31291308,
            "prev7dCount": 5,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 8128612,
            "currCount": 33,
            "fileType": "jpg",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles6/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 8128612,
            "prev7dCount": 33,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 4074795,
            "currCount": 2,
            "fileType": "txt",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/testcontainer/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 4074795,
            "prev7dCount": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 7776,
            "currCount": 1,
            "fileType": "jpg",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 7776,
            "prev7dCount": 1,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 740214000,
            "currCount": 8,
            "fileType": "txt",
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-geo/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 740214000,
            "prev7dCount": 8,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 710880692,
            "currCount": 1,
            "fileType": "tsv",
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "prev30dBytes": 710880692,
            "prev30dCount": 1,
            "prev7dBytes": 710880692,
            "prev7dCount": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 9734926,
            "currCount": 8,
            "fileType": "csv",
            "prev30dBytes": 0,
            "prev30dCount": 6,
            "prev7dBytes": 9734920,
            "prev7dCount": 8,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 5167391,
            "currCount": 1,
            "fileType": "parquet",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 5167391,
            "prev7dCount": 1
        },
        {
            "currBytes": 1825801,
            "currCount": 3,
            "fileType": "jpg",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles4/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 1825801,
            "prev7dCount": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 27265770,
            "currCount": 6,
            "fileType": "pdf",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles3/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 27265770,
            "prev7dCount": 6,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 726,
            "currCount": 1,
            "fileType": "csv",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/testcontainer/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 726,
            "prev7dCount": 1,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 578516260,
            "currCount": 4,
            "fileType": "txt",
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-year/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 578516260,
            "prev7dCount": 4,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 1358360,
            "currCount": 1,
            "fileType": "txt",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/destinationtestcontainer/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 1358360,
            "prev7dCount": 1,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 710880692,
            "currCount": 1,
            "fileType": "tsv",
            "prev30dBytes": 710880692,
            "prev30dCount": 1,
            "prev7dBytes": 710880692,
            "prev7dCount": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 9962189,
            "currCount": 37,
            "fileType": "jpg",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 9962189,
            "prev7dCount": 37,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 710880692,
            "currCount": 1,
            "fileType": "tsv",
            "prev30dBytes": 710880692,
            "prev30dCount": 1,
            "prev7dBytes": 710880692,
            "prev7dCount": 1
        },
        {
            "currBytes": 118811,
            "currCount": 2,
            "fileType": "csv",
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 118811,
            "prev7dCount": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 5167391,
            "currCount": 1,
            "fileType": "parquet",
            "path": "https://fabrikamlake.dfs.core.windows.net/users/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 5167391,
            "prev7dCount": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 7417,
            "currCount": 1,
            "fileType": "csv",
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "prev30dBytes": 7417,
            "prev30dCount": 1,
            "prev7dBytes": 7417,
            "prev7dCount": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 740214000,
            "currCount": 13,
            "fileType": "txt",
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-month/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 740214000,
            "prev7dCount": 13,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 5433155,
            "currCount": 3,
            "fileType": "txt",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 5433155,
            "prev7dCount": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 166707599,
            "currCount": 34,
            "fileType": "pdf",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 166707599,
            "prev7dCount": 34,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 9962189,
            "currCount": 37,
            "fileType": "jpg",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 9962189,
            "prev7dCount": 37
        },
        {
            "currBytes": 17757540,
            "currCount": 3,
            "fileType": "pdf",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles2/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 17757540,
            "prev7dCount": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 6914693,
            "currCount": 3,
            "fileType": "pdf",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles5/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 6914693,
            "prev7dCount": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 15246859,
            "currCount": 3,
            "fileType": "pdf",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles9/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 15246859,
            "prev7dCount": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 740214000,
            "currCount": 9,
            "fileType": "txt",
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-defaultrs/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 740214000,
            "prev7dCount": 9,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 20678283,
            "currCount": 3,
            "fileType": "pdf",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles4/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 20678283,
            "prev7dCount": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 740551400,
            "currCount": 5,
            "fileType": "txt",
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-lang/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 740551400,
            "prev7dCount": 5,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 5167391,
            "currCount": 1,
            "fileType": "parquet",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 5167391,
            "prev7dCount": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 10498044,
            "currCount": 17,
            "fileType": "csv",
            "prev30dBytes": 7411,
            "prev30dCount": 7,
            "prev7dBytes": 10498038,
            "prev7dCount": 17
        },
        {
            "currBytes": 4501375797,
            "currCount": 66,
            "fileType": "txt",
            "prev30dBytes": 122,
            "prev30dCount": 1,
            "prev7dBytes": 4501375797,
            "prev7dCount": 66
        },
        {
            "currBytes": 0,
            "currCount": 6,
            "fileType": "csv",
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "prev30dBytes": 0,
            "prev30dCount": 6,
            "prev7dBytes": 0,
            "prev7dCount": 6,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 527265,
            "currCount": 5,
            "fileType": "csv",
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 527265,
            "prev7dCount": 5,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "currBytes": 9734200,
            "currCount": 1,
            "fileType": "csv",
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/testbes/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 9734200,
            "prev7dCount": 1,
            "sourceType": "Azure Blob Storage"
        },
        {
            "currBytes": 109625,
            "currCount": 1,
            "fileType": "csv",
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "prev30dBytes": 0,
            "prev30dCount": 0,
            "prev7dBytes": 109625,
            "prev7dCount": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        }
    ],
    "snapshotTime": "2021-11-23T13:24:03.729311Z"
}
```
</p>
</details>
