# pv scan readSystemScanRulesetLatest
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesetLatest

## Description
Get the latest version of a system scan ruleset

## Syntax
```
pv scan readSystemScanRulesetLatest --dataSourceType=<val>
```

## Required Arguments
*None*

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
pv scan readSystemScanRulesetLatest --dataSourceType "AzureCosmosDb"
```