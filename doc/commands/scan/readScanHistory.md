# pv scan readScanHistory
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScanHistory

## Description
Lists the scan history of a scan

## Syntax
```
pv scan readScanHistory --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Result > [List Scan History](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-result/list-scan-history)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/runs
```

## Examples
Get the scan history of a scan by data source name and scan name.
```powershell
pv scan readScanHistory --dataSourceName "AzureDataLakeStorage-Gbm" --scanName "Scan-Xei"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 1,
    "value": [
        {
            "assetsClassified": 3,
            "assetsDiscovered": 8,
            "dataSourceType": "AdlsGen2",
            "diagnostics": {
                "exceptionCountMap": {},
                "notifications": []
            },
            "endTime": "2022-02-23T15:52:25.4059244Z",
            "error": null,
            "errorMessage": null,
            "id": "4ea34468-4242-4946-89b2-6bfedb237b10",
            "ingestionJobId": "4ea34468-4242-4946-89b2-6bfedb237b10",
            "parentId": null,
            "pipelineStartTime": "2022-02-23T15:46:30Z",
            "queuedTime": "2022-02-23T15:45:57.7955456Z",
            "resourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/esg/providers/Microsoft.Storage/storageAccounts/esg26fa7f24adls",
            "runType": "Manual",
            "scanLevelType": "Full",
            "scanRulesetType": "System",
            "scanRulesetVersion": 5,
            "startTime": "2022-02-23T15:45:57.5629837Z",
            "status": "Succeeded",
            "webScanResults": null
        }
    ]
}
```
</p>
</details>