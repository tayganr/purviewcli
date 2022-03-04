# pv policystore deleteDataPolicy
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > deleteDataPolicy

## Description
Delete a data policy.

## Syntax
```
pv policystore deleteDataPolicy --policyName=<val>
```

## Required Arguments
`--policyName` (string)  
The name of the data policy.

## Optional Arguments
*None*

## API Mapping
Delete a data policy.
```
DELETE https://{accountName}.purview.azure.com/policystore/dataPolicies/{policyName}
```

## Examples
Delete a data policy.
```powershell
pv policystore deleteDataPolicy --policyName "new-policy"
```