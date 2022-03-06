# pv scan putFilter
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putFilter

## Description
Creates or updates a filter.

## Syntax
```
pv scan putFilter --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
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
Scanning Data Plane > Filters > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/filters/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/filters/custom
```

## Examples
Create or update a scan filter.
```powershell
pv scan putFilter --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-Qrh" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "name": "custom",
    "properties": {
        "excludeUriPrefixes": [
            "https://pvlab4da424adls.dfs.core.windows.net/raw/BingCoronavirusQuerySet"
        ],
        "includeUriPrefixes": [
            "https://pvlab4da424adls.dfs.core.windows.net/",
            "https://pvlab4da424adls.dfs.core.windows.net/raw",
            "https://pvlab4da424adls.dfs.core.windows.net/raw/Twitter"
        ]
    }
}
```
</p>
</details>