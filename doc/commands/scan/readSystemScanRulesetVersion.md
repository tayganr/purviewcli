# pv scan readSystemScanRulesetVersion
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesetVersion

## Description
Get a scan ruleset by version

## Syntax
```
pv scan readSystemScanRulesetVersion --version=<val> --dataSourceType=<val>
```

## Required Arguments
`--version` (integer)  
A system scan ruleset version number.

`--dataSourceType` (string)  
A valid data source type.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [Get By Version](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/get-by-version)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets/versions/{version}
```

## Examples
Get a system scan ruleset by version and data source type.
```powershell
pv scan readSystemScanRulesetVersion --dataSourceType "AmazonMySql" --version 2
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
}
```
</p>
</details>