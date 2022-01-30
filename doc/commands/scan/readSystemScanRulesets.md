# pv scan readSystemScanRulesets
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesets

## Description
List all system scan rulesets for an account.

## Syntax
```
pv scan readSystemScanRulesets
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/list-all)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets
```

## Examples
List all system scan rulesets.
```powershell
pv scan readSystemScanRulesets
```