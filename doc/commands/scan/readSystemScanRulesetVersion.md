# pv scan readSystemScanRulesetVersion
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesetVersion

## Description
Get a scan ruleset by version

## Syntax
```
pv scan readSystemScanRulesetVersion --version=<val> --dataSourceType=<val>
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
Get a system scan ruleset by version and data source type.
```powershell
pv scan readSystemScanRulesetVersion --version 2 --dataSourceType "AzureCosmosDb"
```