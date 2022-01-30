# pv scan readDataSource
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readDataSource

## Description
Get a data source.

## Syntax
```
pv scan readDataSource --dataSourceName=<val>
```

## Required Arguments
*None*

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
pv scan readDataSource --dataSourceName "AzureSqlDatabase-9ZX"
```