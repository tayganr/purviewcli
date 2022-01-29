# pv account getResourceSetRule
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getResourceSetRule

## Description
Get a resource set config service model.

## Syntax
```
pv account getResourceSetRule
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Resource Set Rules > [Get Resource Set Rule](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/resource-set-rules/get-resource-set-rule)
```
GET https://{accountName}.purview.azure.com/account/resourceSetRuleConfigs/defaultResourceSetRuleConfig
```

## Examples
Get a resource set.
```powershell
pv account getResourceSetRule
```