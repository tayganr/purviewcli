# pv scan readScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScanRuleset

## Description
Get a scan ruleset

## Syntax
```
pv scan readScanRuleset --scanRulesetName=<val>
```

## Required Arguments
`--scanRulesetName` (string)  
The scan ruleset name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Rulesets > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-rulesets/get)
```
GET https://{accountName}.purview.azure.com/scan/scanrulesets/{scanRulesetName}
```

## Examples
Get a custom scan ruleset.
```powershell
pv scan readScanRuleset --scanRulesetName "adls_parquet_only"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "scanrulesets/adls_parquet_only",
    "kind": "AdlsGen2",
    "name": "adls_parquet_only",
    "properties": {
        "collection": null,
        "createdAt": "2022-02-27T21:22:19.0970457Z",
        "description": null,
        "excludedSystemClassifications": [],
        "includedCustomClassificationRuleNames": [],
        "lastModifiedAt": "2022-02-27T21:22:19.0970462Z",
        "scanningRule": {
            "customFileExtensions": null,
            "fileExtensions": [
                "PARQUET"
            ]
        },
        "temporaryResourceFilters": [
            {
                "ingestTemporaryResource": true,
                "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
            }
        ]
    },
    "scanRulesetType": "Custom",
    "status": "Enabled",
    "version": 1
}
```
</p>
</details>