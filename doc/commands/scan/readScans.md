# pv scan readScans
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScans

## Description
List scans in data source.

## Syntax
```
pv scan readScans --dataSourceName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scans > [List By Data Source](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scans/list-by-data-source)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans
```

## Examples
List scans in a data source.
```powershell
pv scan readScans --dataSourceName "AzureSqlDatabase-9ZX"
```