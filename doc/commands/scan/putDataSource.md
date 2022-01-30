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
Create or update a data source.
```powershell
pv scan putDataSource --dataSourceName "AzureSqlDatabase-ABC" --payloadFile "/path/to/file.json"  
```

Example payload.
```json
{
    "kind": "AzureSqlDatabase",
    "name": "AzureSqlDatabase-ABC",
    "properties": {
        "collection": {
            "referenceName": "fkcbkx",
            "type": "CollectionReference"
        },
        "location": "westeurope",
        "resourceGroup": "my-rg",
        "resourceId": "/subscriptions/abc123-9876-12ab-12ab-c0d1d2e08ca0/resourceGroups/my-rg/providers/Microsoft.Sql/servers/my-sqlsvr",
        "resourceName": "my-sqlsvr",
        "serverEndpoint": "my-sqlsvr.database.windows.net",
        "subscriptionId": "abc123-9876-12ab-12ab-c0d1d2e08ca0"
    }
}
```