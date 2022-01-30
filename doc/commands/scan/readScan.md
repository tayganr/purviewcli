# pv scan readScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScan

## Description
Gets a scan information

## Syntax
```
pv scan readScan --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scans > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scans/get)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}
```

## Examples
Get a scan by data source name and scan name.
```powershell
pv scan readScan --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-p1E"
```