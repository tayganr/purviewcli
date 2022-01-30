# pv scan deleteScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > deleteScanRuleset

## Description
Deletes a scan ruleset

## Syntax
```
pv scan deleteScanRuleset --scanRulesetName=<val>
```

## Required Arguments
`--scanRulesetName` (string)  
The scan ruleset name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Rulesets > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-rulesets/delete)
```
DELETE https://{accountName}.purview.azure.com/scan/scanrulesets/{scanRulesetName}
```

## Examples
Delete a custom scan ruleset by name.
```powershell
pv scan deleteScanRuleset --scanRulesetName "twitter_scan_rule_set"
```