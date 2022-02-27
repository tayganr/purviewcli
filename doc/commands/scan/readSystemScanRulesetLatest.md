# pv scan readSystemScanRulesetLatest
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesetLatest

## Description
Get the latest version of a system scan ruleset

## Syntax
```
pv scan readSystemScanRulesetLatest --dataSourceType=<val>
```

## Required Arguments
`--dataSourceType` (string)  
A valid data source type.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [Get Latest](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/get-latest)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets/versions/latest
```

## Examples
Get the latest version of a system scan ruleset by data source type.
```powershell
pv scan readSystemScanRulesetLatest --dataSourceType "AmazonMySql"
```
<details><summary>Sample response.</summary>
<p>

```json
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
}
```
</p>
</details>