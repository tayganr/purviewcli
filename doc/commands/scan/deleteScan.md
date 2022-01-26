# pv scan deleteScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > deleteScan

## Description
Deletes the scan associated with the data source

## Syntax
```
pv scan deleteScan --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Scans > Delete](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scans/delete)
```
DELETE https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}
```

## Examples
```powershell

```