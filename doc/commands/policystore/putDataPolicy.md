# pv policystore putDataPolicy
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > putDataPolicy

## Description
Create or update a data policy.

## Syntax
```
pv policystore putDataPolicy --policyName=<val> --payloadFile=<val>
```

## Required Arguments
`--policyName` (string)  
The name of the data policy.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Create or update a data policy.
```
PUT https://{accountName}.purview.azure.com/policystore/dataPolicies/{policyName}
```

## Examples
Create or update a data policy.
```powershell
pv policystore putDataPolicy --policyName "new-policy" --payloadFile "/path/to/file.json"
```

<details><summary>Example payload.</summary>
<p>

```json
{
    "name": "new-policy",
    "properties": {
        "collection": {
            "referenceName": "pvdemocrv3k-pv",
            "type": "CollectionReference"
        },
        "decisionRules": [
            {
                "cnfCondition": [
                    [
                        {
                            "attributeName": "resource.azure.path",
                            "attributeValueIncludedIn": [
                                "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvdemo-rg-crv3k/providers/Microsoft.Storage/storageAccounts/pvdemocrv3kadls/**"
                            ]
                        }
                    ],
                    [
                        {
                            "attributeName": "principal.microsoft.id",
                            "attributeValueIncludedIn": [
                                "095354ff-cae8-44ff-8120-22ec5a941b40"
                            ]
                        }
                    ],
                    [
                        {
                            "attributeName": "derived.purview.role",
                            "attributeValueIncludes": "purviewdatarole_builtin_read",
                            "fromRule": "purviewdatarole_builtin_read"
                        }
                    ]
                ],
                "effect": "Permit",
                "id": "32dcda57-b9a2-4ada-8f58-db8cebe037ac",
                "kind": "decisionrule",
                "updatedAt": "03/04/2022 15:32:15"
            }
        ],
        "description": "Hello World",
        "policyDetails": {
            "policyType": "AccessControl"
        }
    }
}
```
</p>
</details>