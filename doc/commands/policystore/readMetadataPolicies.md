# pv policystore readMetadataPolicies
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataPolicies

## Description
List all metadata policies.

## Syntax
```
pv policystore readMetadataPolicies
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Policy > [List All](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-policy/list-all)
```
GET https://{accountName}.purview.azure.com/policystore/metadataPolicies
```

## Examples
Get all metadata policies.
```powershell
pv policystore readMetadataPolicies
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "values": [
        {
            "id": "a17fef61-3a7d-4453-925c-8cbf7b83af92",
            "name": "policy_YOUR_PURVIEW_ACCOUNT_NAME",
            "properties": {
                "attributeRules": [
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "principal.microsoft.id",
                                    "attributeValueIncludedIn": [
                                        "095354ff-cae8-44ff-8120-22ec5a941b40"
                                    ]
                                },
                                {
                                    "attributeName": "derived.purview.role",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator",
                                    "fromRule": "purviewmetadatarole_builtin_collection-administrator"
                                }
                            ]
                        ],
                        "id": "purviewmetadatarole_builtin_collection-administrator:YOUR_PURVIEW_ACCOUNT_NAME",
                        "kind": "attributerule",
                        "name": "purviewmetadatarole_builtin_collection-administrator:YOUR_PURVIEW_ACCOUNT_NAME"
                    },
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "principal.microsoft.id",
                                    "attributeValueIncludedIn": [
                                        "095354ff-cae8-44ff-8120-22ec5a941b40"
                                    ]
                                },
                                {
                                    "attributeName": "derived.purview.role",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_purview-reader",
                                    "fromRule": "purviewmetadatarole_builtin_purview-reader"
                                }
                            ]
                        ],
                        "id": "purviewmetadatarole_builtin_purview-reader:YOUR_PURVIEW_ACCOUNT_NAME",
                        "kind": "attributerule",
                        "name": "purviewmetadatarole_builtin_purview-reader:YOUR_PURVIEW_ACCOUNT_NAME"
                    },
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "principal.microsoft.id",
                                    "attributeValueIncludedIn": [
                                        "095354ff-cae8-44ff-8120-22ec5a941b40",
                                        "60117586-ca87-4eac-a217-9d130ded9af0"
                                    ]
                                },
                                {
                                    "attributeName": "derived.purview.role",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_data-curator",
                                    "fromRule": "purviewmetadatarole_builtin_data-curator"
                                }
                            ]
                        ],
                        "id": "purviewmetadatarole_builtin_data-curator:YOUR_PURVIEW_ACCOUNT_NAME",
                        "kind": "attributerule",
                        "name": "purviewmetadatarole_builtin_data-curator:YOUR_PURVIEW_ACCOUNT_NAME"
                    },
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "principal.microsoft.id",
                                    "attributeValueIncludedIn": [
                                        "095354ff-cae8-44ff-8120-22ec5a941b40"
                                    ]
                                },
                                {
                                    "attributeName": "derived.purview.role",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_data-source-administrator",
                                    "fromRule": "purviewmetadatarole_builtin_data-source-administrator"
                                }
                            ]
                        ],
                        "id": "purviewmetadatarole_builtin_data-source-administrator:YOUR_PURVIEW_ACCOUNT_NAME",
                        "kind": "attributerule",
                        "name": "purviewmetadatarole_builtin_data-source-administrator:YOUR_PURVIEW_ACCOUNT_NAME"
                    },
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "purviewmetadatarole_builtin_collection-administrator:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ],
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_purview-reader:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "purviewmetadatarole_builtin_purview-reader:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ],
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_data-curator:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "purviewmetadatarole_builtin_data-curator:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ],
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_data-source-administrator:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "purviewmetadatarole_builtin_data-source-administrator:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ]
                        ],
                        "id": "permission:YOUR_PURVIEW_ACCOUNT_NAME",
                        "kind": "attributerule",
                        "name": "permission:YOUR_PURVIEW_ACCOUNT_NAME"
                    }
                ],
                "collection": {
                    "referenceName": "YOUR_PURVIEW_ACCOUNT_NAME",
                    "type": "CollectionReference"
                },
                "decisionRules": [
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "resource.purview.collection",
                                    "attributeValueIncludes": "YOUR_PURVIEW_ACCOUNT_NAME"
                                },
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "permission:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "permission:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ]
                        ],
                        "effect": "Permit",
                        "kind": "decisionrule"
                    }
                ],
                "description": ""
            },
            "version": 1
        },
        {
            "id": "fbd09c5e-4c09-43f4-b22c-535fb85b5075",
            "name": "policy_g7qe97",
            "properties": {
                "attributeRules": [
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "principal.microsoft.id",
                                    "attributeValueIncludedIn": [
                                        "095354ff-cae8-44ff-8120-22ec5a941b40"
                                    ]
                                },
                                {
                                    "attributeName": "derived.purview.role",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator",
                                    "fromRule": "purviewmetadatarole_builtin_collection-administrator"
                                }
                            ],
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "purviewmetadatarole_builtin_collection-administrator:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ]
                        ],
                        "id": "purviewmetadatarole_builtin_collection-administrator:g7qe97",
                        "kind": "attributerule",
                        "name": "purviewmetadatarole_builtin_collection-administrator:g7qe97"
                    },
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:g7qe97",
                                    "fromRule": "purviewmetadatarole_builtin_collection-administrator:g7qe97"
                                }
                            ],
                            [
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "permission:YOUR_PURVIEW_ACCOUNT_NAME",
                                    "fromRule": "permission:YOUR_PURVIEW_ACCOUNT_NAME"
                                }
                            ]
                        ],
                        "id": "permission:g7qe97",
                        "kind": "attributerule",
                        "name": "permission:g7qe97"
                    }
                ],
                "collection": {
                    "referenceName": "g7qe97",
                    "type": "CollectionReference"
                },
                "decisionRules": [
                    {
                        "dnfCondition": [
                            [
                                {
                                    "attributeName": "resource.purview.collection",
                                    "attributeValueIncludes": "g7qe97"
                                },
                                {
                                    "attributeName": "derived.purview.permission",
                                    "attributeValueIncludes": "permission:g7qe97",
                                    "fromRule": "permission:g7qe97"
                                }
                            ]
                        ],
                        "effect": "Permit",
                        "kind": "decisionrule"
                    }
                ],
                "description": "",
                "parentCollectionName": "YOUR_PURVIEW_ACCOUNT_NAME"
            },
            "version": 0
        }
    ]
}
```
</p>
</details>