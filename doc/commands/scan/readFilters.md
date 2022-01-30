# pv scan readFilters
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readFilters

## Description
Get a filter

## Syntax
```
pv scan readFilters --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Filters > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/filters/get)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/filters/custom
```

## Examples
Get scan filters (scope) by data source name and scan name.
```powershell
pv scan readFilters --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-p1E"
```