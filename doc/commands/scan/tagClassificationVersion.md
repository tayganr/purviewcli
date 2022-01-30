# pv scan tagClassificationVersion
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > tagClassificationVersion

## Description
Sets Classification Action on a specific classification rule version.

## Syntax
```
pv scan tagClassificationVersion --classificationRuleName=<val> --classificationRuleVersion=<val> --action=<val>
```

## Required Arguments
`--classificationRuleName` (string)  
The name of the classification rule.

`--classificationRuleVersion` (integer)  
The classification rule version number.

`--action` (string)  
The classification action (Keep or Delete).

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [Tag Classification Version](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/tag-classification-version)
```
POST https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}/versions/{classificationRuleVersion}/:tag
```

## Examples
Set classification action to Keep on a specific classification rule version.
```powershell
pv scan tagClassificationVersion --classificationRuleName "twitter_handle_rule" --classificationRuleVersion 1 --action "Keep"         
```

Set classification action to Delete on a specific classification rule version.
```powershell
pv scan tagClassificationVersion --classificationRuleName "twitter_handle_rule" --classificationRuleVersion 1 --action "Delete"         
```