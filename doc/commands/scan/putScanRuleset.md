# pv scan putScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putScanRuleset

## Description
Creates or Updates a scan ruleset

## Syntax
```
pv scan putScanRuleset --scanRulesetName=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Rulesets > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-rulesets/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/scanrulesets/{scanRulesetName}
```

## Examples
```powershell

```