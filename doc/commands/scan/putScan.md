# pv scan putScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putScan

## Description
Creates an instance of a scan

## Syntax
```
pv scan putScan --dataSourceName=<val> --scanName=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Scans > Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scans/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}
```

## Examples
```powershell

```