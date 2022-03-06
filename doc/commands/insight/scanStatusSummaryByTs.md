# pv insight scanStatusSummaryByTs
[Command Reference](../../../README.md#command-reference) > [insight](./main.md) > scanStatusSummaryByTs

## Description
Total number of scans by status and time period.

## Syntax
```
pv insight scanStatusSummaryByTs [--numberOfDays=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--numberOfDays` (integer)  
Trailing time period in days [default: 30].

## API Mapping
```
GET https://{accountName}.purview.azure.com/mapanddiscover/reports/scanstatus2/summariesbyts
```

## Examples
Get the total number of scans by status and time period.
```powershell
pv insight scanStatusSummaryByTs
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "values": [
        {
            "endTime": "2022-03-12T23:59:59Z",
            "startTime": "2022-03-06T00:00:00Z",
            "summaries": [
                {
                    "count": 0,
                    "type": "Succeeded"
                },
                {
                    "count": 0,
                    "type": "Failed"
                },
                {
                    "count": 0,
                    "type": "Canceled"
                }
            ]
        },
        {
            "endTime": "2022-03-05T23:59:59Z",
            "startTime": "2022-02-27T00:00:00Z",
            "summaries": [
                {
                    "count": 11,
                    "type": "Succeeded"
                },
                {
                    "count": 8,
                    "type": "Failed"
                },
                {
                    "count": 0,
                    "type": "Canceled"
                }
            ]
        },
        {
            "endTime": "2022-02-26T23:59:59Z",
            "startTime": "2022-02-20T00:00:00Z",
            "summaries": [
                {
                    "count": 6,
                    "type": "Succeeded"
                },
                {
                    "count": 0,
                    "type": "Failed"
                },
                {
                    "count": 0,
                    "type": "Canceled"
                }
            ]
        },
        {
            "endTime": "2022-02-19T23:59:59Z",
            "startTime": "2022-02-13T00:00:00Z",
            "summaries": [
                {
                    "count": 5,
                    "type": "Succeeded"
                },
                {
                    "count": 0,
                    "type": "Failed"
                },
                {
                    "count": 0,
                    "type": "Canceled"
                }
            ]
        },
        {
            "endTime": "2022-02-12T23:59:59Z",
            "startTime": "2022-02-06T00:00:00Z",
            "summaries": [
                {
                    "count": 9,
                    "type": "Succeeded"
                },
                {
                    "count": 1,
                    "type": "Failed"
                },
                {
                    "count": 0,
                    "type": "Canceled"
                }
            ]
        },
        {
            "endTime": "2022-02-05T23:59:59Z",
            "startTime": "2022-01-30T00:00:00Z",
            "summaries": [
                {
                    "count": 2,
                    "type": "Succeeded"
                },
                {
                    "count": 0,
                    "type": "Failed"
                },
                {
                    "count": 0,
                    "type": "Canceled"
                }
            ]
        }
    ]
}
```
</p>
</details>
