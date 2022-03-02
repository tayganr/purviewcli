# pv management readAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readAccount

## Description
Gets the account resource.

## Syntax
```
pv management readAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account.

## Optional Arguments
*None*

## API Mapping
Accounts > [Get](https://docs.microsoft.com/en-us/rest/api/purview/accounts/get)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
Get the properties of an existing Azure Purview account.
```powershell
pv management readAccount --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg" --accountName "esg-26fa7f24-pv"
```

<details><summary>Sample response.</summary>
<p>

```json
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
}
```
</p>
</details>