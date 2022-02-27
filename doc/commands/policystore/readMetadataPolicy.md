# pv policystore readMetadataPolicy
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataPolicy

## Description
Gets a metadata policy.

## Syntax
```
pv policystore readMetadataPolicy (--collectionName=<val> | --policyId=<val>)
```

## Required Arguments
`--collectionName` (string)  
This unique name of the collection.

`--policyId` (string)  
The unique policy id.

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Policy > [Get](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-policy/get)
```
GET https://{accountName}.purview.azure.com/policystore/metadataPolicies/{policyId}
```

Get Metadata Policy by Collection Name
```
GET https://{accountName}.purview.azure.com/policystore/collections/{collectionName}/metadataPolicy
```

## Examples
Get a metadata policy by collection name.
```powershell
pv policystore readMetadataPolicy --collectionName "pokuj2"
```

<details><summary>Sample response.</summary>
<p>

```json
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
                            "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:esg-26fa7f24-pv",
                            "fromRule": "purviewmetadatarole_builtin_collection-administrator:esg-26fa7f24-pv"
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
                            "attributeValueIncludes": "permission:esg-26fa7f24-pv",
                            "fromRule": "permission:esg-26fa7f24-pv"
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
        "parentCollectionName": "esg-26fa7f24-pv"
    },
    "version": 0
}
```
</p>
</details>

Get a metadata policy by policy id.
```powershell
pv policystore readMetadataPolicy --policyId "67c667b7-8f1c-468f-ab3b-f19fd943de95"
```