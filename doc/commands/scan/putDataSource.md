# pv scan putDataSource
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putDataSource

## Description
Creates or Updates a data source

## Syntax
```
pv scan putDataSource --dataSourceName=<val> --payloadFile=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Data Sources > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/data-sources/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}
```

## Examples
Create or update a data source - Azure SQL Database.
```powershell
pv scan putDataSource --dataSourceName "AzureSqlDatabase-ABC" --payloadFile "/path/to/file.json"  
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "kind": "AzureSqlDatabase",
    "name": "AzureSqlDatabase-ABC",
    "properties": {
        "serverEndpoint": "my-sqlsvr.database.windows.net",
        "subscriptionId": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0",
        "resourceGroup": "pvlab-taygan",
        "location": "westeurope",
        "resourceName": "my-sqlsvr",
        "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvlab-taygan/providers/Microsoft.Sql/servers/pvlab-e2c824-sqlsvr",
        "collection": {
            "type": "CollectionReference",
            "referenceName": "esg-26fa7f24-pv"
        }
    }
}
```
</p>
</details><br />

Create or update a data source - SQL Server.
```powershell
pv scan putDataSource --dataSourceName "YOUR_DS_NAME" --payloadFile "/path/to/file.json"  
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "kind": "SqlServerDatabase",
    "name": "YOUR_DS_NAME",
    "properties": {
        "serverEndpoint": "YOUR_SQL_ENDPOINT",
        "collection": {
            "type": "CollectionReference",
            "referenceName": "hqzywr"
        }
    }
}
```
</p>
</details>