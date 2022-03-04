# pv policystore putDataPolicyScope
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > putDataPolicyScope

## Description
Create or update a data policy scope.

## Syntax
```
pv policystore putDataPolicyScope --policyName=<val> --payloadFile=<val>
```

## Required Arguments
`--policyName` (string)  
The name of the data policy.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Create or update a data policy scope.
```
PUT https://{accountName}.purview.azure.com/policystore/dataPolicies/{policyName}/scopes
```

## Examples
Create or update a data policy scope.
```powershell
pv policystore putDataPolicyScope --policyName "new-policy" --payloadFile "/path/to/file.json"
```

<details><summary>Example payload.</summary>
<p>

```json
{
    "properties": {
        "dataSourceScope": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourcegroups/pvdemo-rg-crv3k/providers/microsoft.storage/storageaccounts/pvdemocrv3kadls",
        "dataSourceSubscription": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0",
        "datasource": "AzureDataLakeStorage",
        "policyName": "new-policy"
    }
}
```
</p>
</details>