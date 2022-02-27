# pv policystore readMetadataRoles
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataRoles

## Description
Lists the metadata roles.

## Syntax
```
pv policystore readMetadataRoles
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Roles > [List](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-roles/list)
```
GET https://{accountName}.purview.azure.com/policystore/metadataroles
```

## Examples
Get all metadata roles.
```powershell
pv policystore readMetadataRoles
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "nextLink": "https://YOUR_PURVIEW_ACCOUNT.purview.azure.com/policystore/metadataroles?api-version=2021-07-01",
    "values": [
        {
            "id": "purviewmetadatarole_builtin_data-curator",
            "name": "data-curator",
            "properties": {
                "cnfCondition": [
                    [
                        {
                            "attributeName": "request.azure.dataAction",
                            "attributeValueIncludedIn": [
                                "Microsoft.Purview/accounts/data/read",
                                "Microsoft.Purview/accounts/data/write",
                                "Microsoft.Purview/accounts/collection/read",
                                "Microsoft.Purview/accounts/policy/read"
                            ]
                        }
                    ]
                ],
                "friendlyName": "Data Curator",
                "provisioningState": "Provisioned",
                "roleType": "BuiltIn",
                "version": 1
            },
            "type": "Microsoft.Purview/role"
        },
        {
            "id": "purviewmetadatarole_builtin_data-source-administrator",
            "name": "data-source-administrator",
            "properties": {
                "cnfCondition": [
                    [
                        {
                            "attributeName": "request.azure.dataAction",
                            "attributeValueIncludedIn": [
                                "Microsoft.Purview/accounts/source/read",
                                "Microsoft.Purview/accounts/source/write",
                                "Microsoft.Purview/accounts/scan/read",
                                "Microsoft.Purview/accounts/scan/write",
                                "Microsoft.Purview/accounts/collection/read",
                                "Microsoft.Purview/accounts/policy/bind",
                                "Microsoft.Purview/accounts/policy/read"
                            ]
                        }
                    ]
                ],
                "friendlyName": "Data Source Administrator",
                "provisioningState": "Provisioned",
                "roleType": "BuiltIn",
                "version": 1
            },
            "type": "Microsoft.Purview/role"
        },
        {
            "id": "purviewmetadatarole_builtin_collection-administrator",
            "name": "collection-administrator",
            "properties": {
                "cnfCondition": [
                    [
                        {
                            "attributeName": "request.azure.dataAction",
                            "attributeValueIncludedIn": [
                                "Microsoft.Purview/accounts/collection/read",
                                "Microsoft.Purview/accounts/collection/write"
                            ]
                        }
                    ]
                ],
                "friendlyName": "Collection Administrator",
                "provisioningState": "Provisioned",
                "roleType": "BuiltIn",
                "version": 1
            },
            "type": "Microsoft.Purview/role"
        },
        {
            "id": "purviewmetadatarole_builtin_purview-reader",
            "name": "purview-reader",
            "properties": {
                "cnfCondition": [
                    [
                        {
                            "attributeName": "request.azure.dataAction",
                            "attributeValueIncludedIn": [
                                "Microsoft.Purview/accounts/data/read",
                                "Microsoft.Purview/accounts/collection/read"
                            ]
                        }
                    ]
                ],
                "friendlyName": "Purview Reader",
                "provisioningState": "Provisioned",
                "roleType": "BuiltIn",
                "version": 1
            },
            "type": "Microsoft.Purview/role"
        }
    ]
}
```
</p>
</details>