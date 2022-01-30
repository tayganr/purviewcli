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
pv scan readSystemScanRulesetVersions --dataSourceType "AzureCosmosDb"
```