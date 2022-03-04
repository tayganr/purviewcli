# pv scan readDataSources
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readDataSources

## Description
List data sources in Data catalog.

## Syntax
```
pv scan readDataSources [--collectionName=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--collectionName` (string)  
The unique name of the collection.

## API Mapping
Scanning Data Plane > Data Sources > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/data-sources/list-all)
```
GET https://{accountName}.purview.azure.com/scan/datasources
```

Undocumented API.
```
GET https://{accountName}.purview.azure.com/scan/collections/{collectionName}/listDataSources
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
    "count": 10,
    "value": [
        {
            "id": "datasources/AzureSqlDatabase",
            "kind": "AzureSqlDatabase",
            "name": "AzureSqlDatabase",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:36:15.9349828Z",
                    "referenceName": "hqzywr",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:36:15.9349828Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "lastModifiedAt": "2022-03-03T13:36:15.9349828Z",
                "location": "southcentralus",
                "parentCollection": null,
                "resourceGroup": "pvdemo-rg-crv3k",
                "resourceId": null,
                "resourceName": "pvdemocrv3k-sqlsvr",
                "serverEndpoint": "pvdemocrv3k-sqlsvr.database.windows.net",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        },
        {
            "id": "datasources/AzureDataLakeStorage",
            "kind": "AdlsGen2",
            "name": "AzureDataLakeStorage",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:37:49.9678163Z",
                    "referenceName": "kcbxsh",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:37:49.9678163Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "endpoint": "https://pvdemocrv3kadls.dfs.core.windows.net/",
                "lastModifiedAt": "2022-03-03T13:37:49.9678163Z",
                "location": "southcentralus",
                "parentCollection": null,
                "resourceGroup": "pvdemo-rg-crv3k",
                "resourceId": null,
                "resourceName": "pvdemocrv3kadls",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        },
        {
            "id": "datasources/AmazonAccount-QCq",
            "kind": "AmazonAccount",
            "name": "AmazonAccount-QCq",
            "properties": {
                "awsAccountId": "123456789000",
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:50:18.5798631Z",
                    "referenceName": "tdumy6",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:50:18.5798631Z",
                "dataSourceCollectionMovingState": 0,
                "lastModifiedAt": "2022-03-03T13:50:18.5798631Z",
                "parentCollection": null,
                "roleARN": null
            }
        },
        {
            "id": "datasources/AzureSynapseAnalytics-pYQ",
            "kind": "AzureSynapseWorkspace",
            "name": "AzureSynapseAnalytics-pYQ",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:50:33.3113213Z",
                    "referenceName": "tdumy6",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:50:33.3113213Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "dedicatedSqlEndpoint": "pvdemocrv3k-synapse.sql.azuresynapse.net",
                "lastModifiedAt": "2022-03-03T13:50:33.3113213Z",
                "location": "southcentralus",
                "parentCollection": null,
                "resourceGroup": "pvdemo-rg-crv3k",
                "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvdemo-rg-crv3k/providers/Microsoft.Synapse/workspaces/pvdemocrv3k-synapse",
                "resourceName": "pvdemocrv3k-synapse",
                "serverlessSqlEndpoint": "pvdemocrv3k-synapse-ondemand.sql.azuresynapse.net",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        },
        {
            "id": "datasources/Snowflake-lcq",
            "kind": "Snowflake",
            "name": "Snowflake-lcq",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:50:48.9826788Z",
                    "referenceName": "tdumy6",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:50:48.9826788Z",
                "dataSourceCollectionMovingState": 0,
                "host": "myaccount.snowflake.com",
                "lastModifiedAt": "2022-03-03T13:50:48.9826788Z",
                "parentCollection": null
            }
        },
        {
            "id": "datasources/PowerBI-ebh",
            "kind": "PowerBI",
            "name": "PowerBI-ebh",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:51:08.9128642Z",
                    "referenceName": "kcbxsh",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:51:08.9128642Z",
                "dataSourceCollectionMovingState": 0,
                "lastModifiedAt": "2022-03-03T13:51:08.9128642Z",
                "parentCollection": null,
                "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db47"
            }
        },
        {
            "id": "datasources/Cassandra-tho",
            "kind": "Cassandra",
            "name": "Cassandra-tho",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:51:22.0970467Z",
                    "referenceName": "kcbxsh",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:51:22.0970467Z",
                "dataSourceCollectionMovingState": 0,
                "host": "localhost",
                "lastModifiedAt": "2022-03-03T13:51:22.0970467Z",
                "parentCollection": null,
                "port": 9042
            }
        },
        {
            "id": "datasources/GoogleBigQuery-yeY",
            "kind": "GoogleBigQuery",
            "name": "GoogleBigQuery-yeY",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:51:35.9650465Z",
                    "referenceName": "hqzywr",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:51:35.9650465Z",
                "dataSourceCollectionMovingState": 0,
                "lastModifiedAt": "2022-03-03T13:51:35.9650465Z",
                "parentCollection": null,
                "projectId": "123456"
            }
        },
        {
            "id": "datasources/AzureFileStorage-d2n",
            "kind": "AzureFileService",
            "name": "AzureFileStorage-d2n",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:51:50.3431578Z",
                    "referenceName": "hqzywr",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:51:50.3431578Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "endpoint": "https://esg26fa7f24adls.file.core.windows.net/",
                "lastModifiedAt": "2022-03-03T13:51:50.3431578Z",
                "location": "westeurope",
                "parentCollection": null,
                "resourceGroup": "esg",
                "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/esg/providers/Microsoft.Storage/storageAccounts/esg26fa7f24adls",
                "resourceName": "esg26fa7f24adls",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        },
        {
            "id": "datasources/AzureDataLakeStorage-bao",
            "kind": "AdlsGen2",
            "name": "AzureDataLakeStorage-bao",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T15:30:38.5826252Z",
                    "referenceName": "hqzywr",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T15:30:38.5826252Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "endpoint": "https://tayganhackadls.dfs.core.windows.net/",
                "lastModifiedAt": "2022-03-03T15:30:38.5826252Z",
                "location": "eastus",
                "parentCollection": null,
                "resourceGroup": "hack",
                "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/hack/providers/Microsoft.Storage/storageAccounts/tayganhackadls",
                "resourceName": "tayganhackadls",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        }
    ]
}
```
</p>
</details><br/>

List all data sources within a specific collection.
```powershell
pv scan readDataSources --collectionName "tdumy6"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 3,
    "value": [
        {
            "id": "datasources/AmazonAccount-QCq",
            "kind": "AmazonAccount",
            "name": "AmazonAccount-QCq",
            "properties": {
                "awsAccountId": "123456789000",
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:50:18.5798631Z",
                    "referenceName": "tdumy6",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:50:18.5798631Z",
                "dataSourceCollectionMovingState": 0,
                "lastModifiedAt": "2022-03-03T13:50:18.5798631Z",
                "parentCollection": null,
                "roleARN": null
            }
        },
        {
            "id": "datasources/AzureSynapseAnalytics-pYQ",
            "kind": "AzureSynapseWorkspace",
            "name": "AzureSynapseAnalytics-pYQ",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:50:33.3113213Z",
                    "referenceName": "tdumy6",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:50:33.3113213Z",
                "dataSourceCollectionMovingState": 0,
                "dataUseGovernance": "Disabled",
                "dedicatedSqlEndpoint": "pvdemocrv3k-synapse.sql.azuresynapse.net",
                "lastModifiedAt": "2022-03-03T13:50:33.3113213Z",
                "location": "southcentralus",
                "parentCollection": null,
                "resourceGroup": "pvdemo-rg-crv3k",
                "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvdemo-rg-crv3k/providers/Microsoft.Synapse/workspaces/pvdemocrv3k-synapse",
                "resourceName": "pvdemocrv3k-synapse",
                "serverlessSqlEndpoint": "pvdemocrv3k-synapse-ondemand.sql.azuresynapse.net",
                "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
            }
        },
        {
            "id": "datasources/Snowflake-lcq",
            "kind": "Snowflake",
            "name": "Snowflake-lcq",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-03-03T13:50:48.9826788Z",
                    "referenceName": "tdumy6",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-03-03T13:50:48.9826788Z",
                "dataSourceCollectionMovingState": 0,
                "host": "myaccount.snowflake.com",
                "lastModifiedAt": "2022-03-03T13:50:48.9826788Z",
                "parentCollection": null
            }
        }
    ]
}
```
</p>
</details>