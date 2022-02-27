# pv scan readSystemScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRuleset

## Description
Get a system scan ruleset for a data source.

## Syntax
```
pv scan readSystemScanRuleset --dataSourceType=<val>
```

## Required Arguments
`--dataSourceType` (string)  
A valid data source type.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/get)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets/datasources/{dataSourceType}
```

## Examples
Get a system scan ruleset by data source type.
```powershell
pv scan readSystemScanRuleset --dataSourceType "AmazonMySql"
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