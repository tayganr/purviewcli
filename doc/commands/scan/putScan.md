# pv scan putScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putScan

## Description
Creates an instance of a scan

## Syntax
```
pv scan putScan --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scans > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scans/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}
```

## Examples
Create a scan.
```powershell
pv scan putScan --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-ABC" --payloadFile "/Path/to/file.json"
```

Example payload.
```json
{
    "kind": "AdlsGen2Msi",
    "name": "Scan-ABC",
    "properties": {
        "collection": {
            "referenceName": "fkcbkx",
            "type": "CollectionReference"
        },
        "scanRulesetName": "AdlsGen2",
        "scanRulesetType": "System"
    }
}
```