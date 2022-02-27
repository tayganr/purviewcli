# pv scan readFilters
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readFilters

## Description
Get a filter

## Syntax
```
pv scan readFilters --dataSourceName=<val> --scanName=<val>
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Filters > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/filters/get)
```
GET https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/filters/custom
```

## Examples
Get scan filters (scope) by data source name and scan name.
```powershell
pv scan readFilters --dataSourceName "AzureDataLakeStorage-Gbm" --scanName "Scan-5Jc"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "datasources/AzureDataLakeStorage-Gbm/scans/Scan-5Jc/filters/custom",
    "name": "custom",
    "properties": {
        "excludeRegexes": null,
        "excludeUriPrefixes": [
            "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze",
            "https://esg26fa7f24adls.dfs.core.windows.net/02-silver",
            "https://esg26fa7f24adls.dfs.core.windows.net/esg26fa7f24fs"
        ],
        "includeRegexes": null,
        "includeUriPrefixes": [
            "https://esg26fa7f24adls.dfs.core.windows.net/",
            "https://esg26fa7f24adls.dfs.core.windows.net/03-gold"
        ]
    }
}
```
</p>
</details>