# pv scan readClassificationRules
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readClassificationRules

## Description
List classification rules.

## Syntax
```
pv scan readClassificationRules
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/list-all)
```
GET https://{accountName}.purview.azure.com/scan/classificationrules
```

## Examples
List custom classification rules.
```powershell
pv scan readClassificationRules
```