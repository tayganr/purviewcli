# pv policystore readDataPolicyScopes
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readDataPolicyScopes

## Description
Get data policies.

## Syntax
```
pv policystore readDataPolicyScopes --policyName=<val>
```

## Required Arguments
`--policyName` (string)  
The name of the data policy.

## Optional Arguments
*None*

## API Mapping
Get all scopes for a particular data policy.
```
GET https://{accountName}.purview.azure.com/policystore/dataPolicies/{policyName}/scopes
```

## Examples
Get all scopes for a particular data policy.
```powershell
pv policystore readDataPolicyScopes --policyName "new-policy"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 1,
    "values": [
        {
            "bindingId": "aa280ddf-557c-40a2-b7a6-af8863727ab2",
            "properties": {
                "dataSourceScope": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourcegroups/pvdemo-rg-crv3k/providers/microsoft.storage/storageaccounts/pvdemocrv3kadls",
                "dataSourceSubscription": "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0",
                "datasource": "AzureDataLakeStorage",
                "policyName": "new-policy",
                "systemData": {
                    "createdAt": "2022-03-04T15:36:56.8153903Z",
                    "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                    "lastModifiedAt": "2022-03-04T15:36:56.8153903Z"
                }
            }
        }
    ]
}
```
</p>
</details>