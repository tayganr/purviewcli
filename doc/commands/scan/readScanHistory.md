# pv scan readScanHistory
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScanHistory

## Description
Lists the scan history of a scan

## Syntax
```
pv scan readScanHistory --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Scan Result > List Scan History](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-result/list-scan-history)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/runs
```

## Examples
```powershell

```