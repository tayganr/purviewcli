# pv policystore deleteDataPolicyScope
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > deleteDataPolicyScope

## Description
Delete a data policy scope.

## Syntax
```
pv policystore deleteDataPolicyScope --policyName=<val> --datasource=<val>
```

## Required Arguments
`--policyName` (string)  
The name of the data policy.

`--datasource` (string)  
The name of the data source.

## Optional Arguments
*None*

## API Mapping
Delete a scope associated to an existing data policy.
```
DELETE https://{accountName}.purview.azure.com/policystore/dataPolicies/{policyName}/scopes/{datasource}
```

## Examples
Delete a scope associated to an existing data policy.
```powershell
pv policystore deleteDataPolicyScope --policyName "new-policy" --scopeName "AzureDataLakeStorage"
```