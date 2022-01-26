# pv scan cancelScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > cancelScan

## Description
Cancels a scan

## Syntax
```
pv scan cancelScan --dataSourceName=<val> --scanName=<val> --runId=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Scan Result > Cancel Scan](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-result/cancel-scan)
```
POST https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/runs/{runId}/:cancel
```

## Examples
```powershell

```