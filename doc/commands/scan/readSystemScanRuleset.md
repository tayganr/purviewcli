# pv scan readSystemScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRuleset

## Description
Get a system scan ruleset for a data source.

## Syntax
```
pv scan readSystemScanRuleset --dataSourceType=<val>
```

## Required Arguments
*None*

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
pv scan readSystemScanRuleset --dataSourceType "AzureCosmosDb"
```