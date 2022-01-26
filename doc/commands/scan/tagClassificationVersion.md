# pv scan tagClassificationVersion
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > tagClassificationVersion

## Description
Sets Classification Action on a specific classification rule version.

## Syntax
```
pv scan tagClassificationVersion --classificationRuleName=<val> --classificationRuleVersion=<val> --action=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Classification Rules > Tag Classification Version](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/tag-classification-version)
```
POST https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}/versions/{classificationRuleVersion}/:tag
```

## Examples
```powershell

```