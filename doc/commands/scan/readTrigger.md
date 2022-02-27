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
pv scan readTrigger --dataSourceName "AzureDataLakeStorage-Gbm" --scanName "Scan-5Jc"
```
<details><summary>Sample response.</summary>
<p>

```json
{   
    "id": "datasources/AzureDataLakeStorage-Gbm/scans/Scan-5Jc/triggers/default",
    "name": "default",
    "properties": {
        "createdAt": "2022-02-27T20:26:52.086397Z",
        "lastModifiedAt": "2022-02-27T20:26:52.086397Z",
        "lastScheduled": null,
        "recurrence": {
            "endTime": null,
            "frequency": "Month",
            "interval": 1,
            "schedule": {
                "hours": null,
                "minutes": null,
                "monthDays": [
                    15
                ],
                "monthlyOccurrences": null,
                "weekDays": null
            },
            "startTime": "2022-02-27T20:25:00Z",
            "timezone": "UTC"
        },
        "recurrenceInterval": null,
        "scanLevel": "Incremental"
    }
}
```
</p>
</details>