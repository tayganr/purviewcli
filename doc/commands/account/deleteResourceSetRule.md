# pv account deleteResourceSetRule
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > deleteResourceSetRule

## Description
Delete a resource set.

## Syntax
```
pv account deleteResourceSetRule
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Resource Set Rules > [Delete Resource Set Rule](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/resource-set-rules/delete-resource-set-rule)
```
DELETE https://{accountName}.purview.azure.com/account/resourceSetRuleConfigs/defaultResourceSetRuleConfig
```

## Examples
Delete a resource set.
```powershell
pv account deleteResourceSetRule
```