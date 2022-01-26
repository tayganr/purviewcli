# pv scan putTrigger
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putTrigger

## Description
Creates an instance of a trigger

## Syntax
```
pv scan putTrigger --dataSourceName=<val> --scanName=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Triggers > Create Trigger](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/triggers/create-trigger)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/triggers/default
```

## Examples
```powershell

```