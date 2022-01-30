# pv scan putFilter
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putFilter

## Description
Creates or updates a filter

## Syntax
```
pv scan putFilter --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Filters > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/filters/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/filters/custom
```

## Examples
```powershell

```