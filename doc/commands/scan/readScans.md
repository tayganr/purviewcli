# pv scan readScans
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScans

## Description
List scans in data source.

## Syntax
```
pv scan readScans --dataSourceName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scans > [List By Data Source](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scans/list-by-data-source)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans
```

## Examples
List scans in a data source.
```powershell
pv scan readScans --dataSourceName "AzureDataLakeStorage-Gbm"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "value": [
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
        },
        {
            "id": "datasources/AzureDataLakeStorage-Gbm/scans/Scan-5Jc",
            "kind": "AdlsGen2Msi",
            "name": "Scan-5Jc",
            "properties": {
                "collection": {
                    "lastModifiedAt": "2022-02-27T20:26:51.1585438Z",
                    "referenceName": "esg-26fa7f24-pv",
                    "type": "CollectionReference"
                },
                "createdAt": "2022-02-27T20:26:51.1585438Z",
                "lastModifiedAt": "2022-02-27T20:29:51.4488154Z",
                "scanRulesetName": "AdlsGen2",
                "scanRulesetType": "System"
            }
        }
    ]
}
```
</p>
</details>