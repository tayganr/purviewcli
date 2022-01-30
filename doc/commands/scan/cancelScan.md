# pv scan cancelScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > cancelScan

## Description
Cancels a scan

## Syntax
```
pv scan cancelScan --dataSourceName=<val> --scanName=<val> --runId=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

`--runId` (string)  
The unique ID of the scan run.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Result > [Cancel Scan](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-result/cancel-scan)
```
POST https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/runs/{runId}/:cancel
```

## Examples
Cancel a scan run by data source name, scan name, and run id.
```powershell
pv scan cancelScan --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-p1E" --runId "4b6ee19a-33f8-4b97-92bf-71cce074ba30"
```