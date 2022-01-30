# pv scan deleteDataSource
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > deleteDataSource

## Description
Deletes a data source.

## Syntax
```
pv scan deleteDataSource --dataSourceName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Data Sources > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/data-sources/delete)
```
DELETE https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}
```

## Examples
Delete a data source.
```powershell
pv scan deleteDataSource --dataSourceName "AzureSynapseAnalytics-Wke"
```