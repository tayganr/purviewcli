# pv scan putTrigger
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putTrigger

## Description
Creates an instance of a trigger

## Syntax
```
pv scan putTrigger --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
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
Scanning Data Plane > Triggers > [Create Trigger](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/triggers/create-trigger)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/triggers/default
```

## Examples
Create a trigger and associate it to a scan.
```powershell
pv scan putTrigger --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-Qrh" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "name": "default",
    "properties": {
        "recurrence": {
            "endTime": null,
            "frequency": "Month",
            "interval": 1,
            "schedule": {
                "hours": null,
                "minutes": null,
                "monthDays": [
                    17
                ],
                "monthlyOccurrences": null,
                "weekDays": null
            },
            "startTime": "2022-01-30T12:21:00Z",
            "timezone": "UTC"
        },
        "recurrenceInterval": null,
        "scanLevel": "Incremental"
    }
}
```
</p>
</details>