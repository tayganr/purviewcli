# pv policystore readDataPolicies
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readDataPolicies

## Description
Get data policies.

## Syntax
```
pv policystore readDataPolicies [--policyName=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--policyName` (string)  
The name of the data policy.

## API Mapping
Get all data policies.
```
GET https://{accountName}.purview.azure.com/policystore/dataPolicies
```

Get a specific data policy.
```
GET https://{accountName}.purview.azure.com/policystore/dataPolicies/{policyName}
```

## Examples
Get all data polciies.
```powershell
pv policystore readDataPolicies
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "values": [
        {
            "id": "5a2ce46d-a901-4493-9cf0-472c61a10735",
            "name": "another-policy",
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
                        "id": "33a11019-6fd2-4912-975a-a607718e184e",
                        "kind": "decisionrule",
                        "updatedAt": "03/04/2022 15:41:43"
                    },
                    {
                        "cnfCondition": [
                            [
                                {
                                    "attributeName": "resource.azure.path",
                                    "attributeValueIncludedIn": [
                                        "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pvdemo-rg-crv3k/providers/Microsoft.Storage/storageAccounts/pvdemocrv3kadls/blobServices/default/containers/twitter/blobs/twitter_handles.parquet"
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
                                    "attributeValueIncludes": "purviewdatarole_builtin_modify",
                                    "fromRule": "purviewdatarole_builtin_modify"
                                }
                            ]
                        ],
                        "effect": "Permit",
                        "id": "9082e2da-4c3c-4bfc-b83e-fa9f100a9a98",
                        "kind": "decisionrule",
                        "updatedAt": "03/04/2022 15:41:43"
                    }
                ],
                "description": "This is the second policy.",
                "policyDetails": {
                    "policyType": "AccessControl"
                },
                "systemData": {
                    "createdAt": "2022-03-04T15:41:43.0130397Z",
                    "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                    "lastModifiedAt": "2022-03-04T15:41:43.0130397Z",
                    "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40"
                },
                "version": 1
            }
        },
        {
            "id": "a57ead79-3a14-4256-8113-76fb01c966f2",
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
                },
                "systemData": {
                    "createdAt": "2022-03-04T15:32:15.2650437Z",
                    "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                    "lastModifiedAt": "2022-03-04T15:32:15.2650437Z",
                    "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40"
                },
                "version": 2
            }
        }
    ]
}
```
</p>
</details><br/>

Get a specific data policy by name.
```powershell
pv policystore readDataPolicies --policyName "new-policy"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "a57ead79-3a14-4256-8113-76fb01c966f2",
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
        },
        "systemData": {
            "createdAt": "2022-03-04T15:32:15.2650437Z",
            "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
            "lastModifiedAt": "2022-03-04T15:32:15.2650437Z",
            "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40"
        },
        "version": 2
    }
}
```
</p>
</details>