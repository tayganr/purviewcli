# pv management readAccounts
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readAccounts

## Description
Gets the accounts resources by subscription.

## Syntax
```
pv management readAccounts --subscriptionId=<val> [--resourceGroupName=<val>]
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

## Optional Arguments
`--resourceGroupName` (string)  
The resource group name.

## API Mapping
Accounts > [List By Subscription](https://docs.microsoft.com/en-us/rest/api/purview/accounts/list-by-subscription)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Purview/accounts
```

## Examples
Get all Azure Purview accounts within a particular Azure subscription.
```powershell
pv management readAccounts --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "value": [
        {
            "id": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/esg/providers/Microsoft.Purview/accounts/my-purview-account",
            "identity": {
                "principalId": "PRINCIPAL_ID",
                "tenantId": "TENANT_ID",
                "type": "SystemAssigned"
            },
            "location": "westeurope",
            "name": "my-purview-account",
            "properties": {
                "cloudConnectors": {
                    "awsExternalId": "AWS_EXTERNAL_ID"
                },
                "createdAt": "2022-02-23T09:46:46.2381767Z",
                "createdBy": "email@domain.com",
                "createdByObjectId": "AZURE_AD_OBJECT_ID",
                "endpoints": {
                    "catalog": "https://my-purview-account.purview.azure.com/catalog",
                    "guardian": "https://my-purview-account.purview.azure.com/guardian",
                    "scan": "https://my-purview-account.purview.azure.com/scan"
                },
                "friendlyName": "My Azure Purview Account",
                "managedResourceGroupName": "managed-rg-my-purview-account",
                "managedResources": {
                    "eventHubNamespace": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/managed-rg-my-purview-account/providers/Microsoft.EventHub/namespaces/Atlas-9c27fcd9-17b1-468b-9009-f9d920ed3c58",
                    "resourceGroup": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/managed-rg-my-purview-account",
                    "storageAccount": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/managed-rg-my-purview-account/providers/Microsoft.Storage/storageAccounts/scanwesteuropemxfcqst"
                },
                "privateEndpointConnections": [],
                "provisioningState": "Succeeded",
                "publicNetworkAccess": "Enabled",
                "systemData": {
                    "createdAt": "2022-02-23T09:46:46.2381767Z",
                    "createdBy": "email@domain.com",
                    "createdByType": "User",
                    "lastModifiedAt": "2022-02-23T09:46:46.2381767Z",
                    "lastModifiedBy": "email@domain.com",
                    "lastModifiedByType": "User"
                }
            },
            "sku": {
                "capacity": 1,
                "name": "Standard"
            },
            "tags": {},
            "type": "Microsoft.Purview/accounts"
        },
        {
            "id": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/sandbox/providers/Microsoft.Purview/accounts/another-purview-account",
            "identity": {
                "principalId": "PRINCIPAL_ID",
                "tenantId": "TENANT_ID",
                "type": "SystemAssigned"
            },
            "location": "westeurope",
            "name": "another-purview-account",
            "properties": {
                "cloudConnectors": {
                    "awsExternalId": "AWS_EXTERNAL_ID"
                },
                "createdAt": "2022-03-02T14:45:24.8481086Z",
                "createdBy": "email@domain.com",
                "createdByObjectId": "AZURE_AD_OBJECT_ID",
                "endpoints": {
                    "catalog": "https://another-purview-account.purview.azure.com/catalog",
                    "guardian": "https://another-purview-account.purview.azure.com/guardian",
                    "scan": "https://another-purview-account.purview.azure.com/scan"
                },
                "friendlyName": "another-purview-account",
                "managedResourceGroupName": "managed-rg-another-purview-account",
                "managedResources": {
                    "eventHubNamespace": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/managed-rg-another-purview-account/providers/Microsoft.EventHub/namespaces/Atlas-c04cd008-e661-4c44-acec-29d7097a72a4",
                    "resourceGroup": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/managed-rg-another-purview-account",
                    "storageAccount": "/subscriptions/AZURE_SUBSCRIPTION_ID/resourceGroups/managed-rg-another-purview-account/providers/Microsoft.Storage/storageAccounts/scanwesteuropefckmurj"
                },
                "privateEndpointConnections": [],
                "provisioningState": "Creating",
                "publicNetworkAccess": "Enabled",
                "systemData": {
                    "createdAt": "2022-03-02T14:45:24.8481086Z",
                    "createdBy": "email@domain.com",
                    "createdByType": "User",
                    "lastModifiedAt": "2022-03-02T14:45:24.8481086Z",
                    "lastModifiedBy": "email@domain.com",
                    "lastModifiedByType": "User"
                }
            },
            "sku": {
                "capacity": 1,
                "name": "Standard"
            },
            "tags": {},
            "type": "Microsoft.Purview/accounts"
        }
    ]
}
```
</p>
</details><br />

Get all Azure Purview accounts within a particular resource group.
```powershell
pv management readAccounts --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg"
```