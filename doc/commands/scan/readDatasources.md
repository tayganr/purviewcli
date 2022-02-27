# pv scan readDataSources
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readDataSources

## Description
List data sources in Data catalog.

## Syntax
```
pv scan readDataSources
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Data Sources > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/data-sources/list-all)
```
GET https://{accountName}.purview.azure.com/scan/datasources
```

## Examples
List all data sources.
```powershell
pv scan readDataSources
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 3,
    "value": [
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
        },
        {
            "id": "datasources/AzureSqlDatabase-L5v",
            "kind": "AzureSqlDatabase",
            "name": "AzureSqlDatabase-L5v",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-02-27T20:44:27.2724589Z",
                    "referenceName": "esg-26fa7f24-pv",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-02-27T20:44:27.2724589Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "lastModifiedAt": "2022-02-27T20:44:27.2724589Z",
                "location": "westeurope",
                "parentCollection": null,
                "resourceGroup": "pvlab-taygan",
                "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvlab-taygan/providers/Microsoft.Sql/servers/pvlab-e2c824-sqlsvr",
                "resourceName": "pvlab-e2c824-sqlsvr",
                "serverEndpoint": "pvlab-e2c824-sqlsvr.database.windows.net",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        },
        {
            "id": "datasources/AzureSqlDatabase-ABC",
            "kind": "AzureSqlDatabase",
            "name": "AzureSqlDatabase-ABC",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-02-27T20:47:26.9929916Z",
                    "referenceName": "esg-26fa7f24-pv",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-02-27T20:47:26.9929916Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "lastModifiedAt": "2022-02-27T20:47:26.9929916Z",
                "location": "westeurope",
                "parentCollection": null,
                "resourceGroup": "pvlab-taygan",
                "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvlab-taygan/providers/Microsoft.Sql/servers/pvlab-e2c824-sqlsvr",
                "resourceName": "my-sqlsvr",
                "serverEndpoint": "my-sqlsvr.database.windows.net",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        }
    ]
}
```
</p>
</details>