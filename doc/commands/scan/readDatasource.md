# pv scan readDataSource
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readDataSource

## Description
Get a data source.

## Syntax
```
pv scan readDataSource --dataSourceName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Data Sources > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/data-sources/get)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}
```

## Examples
Get a data source.
```powershell
pv scan readDataSource --dataSourceName "AzureDataLakeStorage-Gbm"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "datasources/AzureDataLakeStorage-Gbm",
    "kind": "AdlsGen2",
    "name": "AzureDataLakeStorage-Gbm",
    "properties": {
        "collection": {
            "lastModifiedAt": "2022-02-23T15:45:16.5674969Z",
            "referenceName": "esg-26fa7f24-pv",
            "type": "CollectionReference"
        },
        "createdAt": "2022-02-23T15:45:16.5674969Z",
        "dataSourceCollectionMovingState": 0,
        "dataUseGovernance": "Disabled",
        "endpoint": "https://esg26fa7f24adls.dfs.core.windows.net/",
        "lastModifiedAt": "2022-02-23T15:45:16.5674969Z",
        "location": "westeurope",
        "parentCollection": null,
        "resourceGroup": "esg",
        "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/esg/providers/Microsoft.Storage/storageAccounts/esg26fa7f24adls",
        "resourceName": "esg26fa7f24adls",
        "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
    }
}
```
</p>
</details>