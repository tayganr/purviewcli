# pv scan putScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putScanRuleset

## Description
Creates or Updates a scan ruleset

## Syntax
```
pv scan putScanRuleset --scanRulesetName=<val> --payloadFile=<val>
```

## Required Arguments
`--scanRulesetName` (string)  
The ruleset name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Rulesets > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-rulesets/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/scanrulesets/{scanRulesetName}
```

## Examples
Create a scan ruleset.
```powershell
pv scan putScanRuleset --scanRulesetName "my_ruleset" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "kind": "AdlsGen2",
    "name": "my_ruleset",
    "properties": {
        "excludedSystemClassifications": [
            "MICROSOFT.GOVERNMENT.CYPRUS.TAX.IDENTIFICATION.NUMBER",
            "MICROSOFT.GOVERNMENT.CHILE.CDI_NUMBER",
            "MICROSOFT.GOVERNMENT.MALTA.DRIVERS.LICENSE.NUMBER"
        ],
        "includedCustomClassificationRuleNames": [],
        "scanningRule": {
            "customFileExtensions": null,
            "fileExtensions": [
                "PARQUET"
            ]
        }
    },
    "scanRulesetType": "Custom"
}
```
</p>
</details>