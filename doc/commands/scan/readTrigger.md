# pv scan readTrigger
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readTrigger

## Description
Gets trigger information

## Syntax
```
pv scan readTrigger --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Triggers > [Get Trigger](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/triggers/get-trigger)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/triggers/default
```

## Examples
Get trigger information for a scan by data source name and scan name.
```powershell
pv scan readTrigger --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-p1E"
```