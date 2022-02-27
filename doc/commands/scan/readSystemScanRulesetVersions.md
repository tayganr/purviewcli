# pv scan readSystemScanRulesetVersions
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesetVersions

## Description
List system scan ruleset versions in Data catalog

## Syntax
```
pv scan readSystemScanRulesetVersions --dataSourceType=<val>
```

## Required Arguments
`--dataSourceType` (string)  
A valid data source type.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [List Versions By Data Source](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/list-versions-by-data-source)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets/versions
```

## Examples
List system scan ruleset versions by data source type.
```powershell
pv scan readSystemScanRulesetVersions --dataSourceType "AmazonMySql" 
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 3,
    "value": [
        {
            "id": "systemscanrulesets/AmazonMySql",
            "kind": "AmazonMySql",
            "name": "AmazonMySql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:49.8617837Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:49.8617837Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AmazonMySql",
            "kind": "AmazonMySql",
            "name": "AmazonMySql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T08:33:29.8537365Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T08:33:29.8537365Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 2
        },
        {
            "id": "systemscanrulesets/AmazonMySql",
            "kind": "AmazonMySql",
            "name": "AmazonMySql",
            "properties": {
                "collection": null,
                "createdAt": "2021-07-18T10:09:24.1602619Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-07-18T10:09:24.1602619Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 1
        }
    ]
}
```
</p>
</details>