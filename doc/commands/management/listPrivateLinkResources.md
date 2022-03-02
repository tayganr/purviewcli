# pv management listPrivateLinkResources
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > listPrivateLinkResources

## Description
Gets a list of privately linkable resources for an account

## Syntax
```
pv management listPrivateLinkResources --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> [--groupId=<val>]
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account.

## Optional Arguments
`--groupId` (string)  
The group identifier.

## API Mapping
Private Link Resources > [List By Account](https://docs.microsoft.com/en-us/rest/api/purview/private-link-resources/list-by-account)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateLinkResources
```

## Examples
List privately linkable resources for an existing Azure Purview account.
```powershell
pv management listPrivateLinkResources --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg" --accountName "esg-26fa7f24-pv"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "value": [
        {
            "id": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/esg/providers/Microsoft.Purview/accounts/esg-26fa7f24-pv/privateLinkResources/account",
            "name": "account",
            "properties": {
                "groupId": "account",
                "requiredMembers": [
                    "account"
                ],
                "requiredZoneNames": [
                    "privatelink.purview.azure.com"
                ]
            },
            "type": "Microsoft.Purview/accounts/privateLinkResources"
        },
        {
            "id": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/esg/providers/Microsoft.Purview/accounts/esg-26fa7f24-pv/privateLinkResources/portal",
            "name": "portal",
            "properties": {
                "groupId": "portal",
                "requiredMembers": [
                    "portal"
                ],
                "requiredZoneNames": [
                    "privatelink.purviewstudio.azure.com"
                ]
            },
            "type": "Microsoft.Purview/accounts/privateLinkResources"
        }
    ]
}
```
</p>
</details>