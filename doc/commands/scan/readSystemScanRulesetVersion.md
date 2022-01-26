# pv scan readSystemScanRulesetVersion
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesetVersion

## Description
Get a scan ruleset by version

## Syntax
```
pv scan readSystemScanRulesetVersions --dataSourceType=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [Get By Version](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/get-by-version)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets/versions/{version}
```

## Examples
```powershell

```