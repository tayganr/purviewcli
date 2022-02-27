# pv scan readScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScan

## Description
Gets a scan information

## Syntax
```
pv scan readScan --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

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
pv scan readScan --dataSourceName "AzureDataLakeStorage-Gbm" --scanName "Scan-Xei"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "datasources/AzureDataLakeStorage-Gbm/scans/Scan-Xei",
    "kind": "AdlsGen2Msi",
    "name": "Scan-Xei",
    "properties": {
        "collection": {
            "lastModifiedAt": "2022-02-23T15:45:56.3612911Z",
            "referenceName": "esg-26fa7f24-pv",
            "type": "CollectionReference"
        },
        "createdAt": "2022-02-23T15:45:56.3612911Z",
        "lastModifiedAt": "2022-02-23T15:45:56.3612911Z",
        "scanRulesetName": "AdlsGen2",
        "scanRulesetType": "System"
    }
}
```
</p>
</details>