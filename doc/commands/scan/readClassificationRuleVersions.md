# pv scan readClassificationRuleVersions
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readClassificationRuleVersions

## Description
Lists the rule versions of a classification rule

## Syntax
```
pv scan readClassificationRuleVersions --classificationRuleName=<val>
```

## Required Arguments
`--classificationRuleName` (string)  
The name of the classification rule.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [List Versions By Classification Rule Name](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/list-versions-by-classification-rule-name)
```
GET https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}/versions
```

## Examples
Get classification rule versions by name.
```powershell
pv scan readClassificationRuleVersions --classificationRuleName "twitter_handle"
```