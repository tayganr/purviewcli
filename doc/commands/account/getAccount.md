# pv account getAccount
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getAccount

## Description
Get an account.

## Syntax
```
pv account getAccount
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Accounts > [Get Account Properties](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/accounts/get-account-properties)
```
GET https://{accountName}.purview.azure.com/account
```

## Examples
Get account properties.
```powershell
pv account getAccount
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/YOUR_RESOURCE_GROUP/providers/Microsoft.Purview/accounts/YOUR_PURVIEW_ACCOUNT_NAME",
    "identity": {
        "principalId": "YOUR_PRINCIPAL_ID",
        "tenantId": "YOUR_TENANT_ID",
        "type": "SystemAssigned"
    },
    "location": "westeurope",
    "name": "YOUR_PURVIEW_ACCOUNT_NAME",
    "properties": {
        "cloudConnectors": {
            "awsExternalId": "YOUR_AWS_EXTERNAL_ID"
        },
        "createdAt": "2022-02-23T09:46:46.2381767Z",
        "createdBy": "EMAIL@DOMAIN.COM",
        "createdByObjectId": "AZURE_AD_OBJECT_ID",
        "endpoints": {
            "catalog": "https://YOUR_PURVIEW_ACCOUNT_NAME.purview.azure.com/catalog",
            "guardian": "https://YOUR_PURVIEW_ACCOUNT_NAME.purview.azure.com/guardian",
            "scan": "https://YOUR_PURVIEW_ACCOUNT_NAME.purview.azure.com/scan"
        },
        "friendlyName": "YOUR_FRIENDLY_PURVIEW_ACCOUNT_NAME",
        "managedResourceGroupName": "managed-rg-YOUR_PURVIEW_ACCOUNT_NAME",
        "managedResources": {
            "eventHubNamespace": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/managed-rg-YOUR_PURVIEW_ACCOUNT_NAME/providers/Microsoft.EventHub/namespaces/YOUR_EVENT_HUB",
            "resourceGroup": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/managed-rg-YOUR_PURVIEW_ACCOUNT_NAME",
            "storageAccount": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/managed-rg-YOUR_PURVIEW_ACCOUNT_NAME/providers/Microsoft.Storage/storageAccounts/YOUR_STORAGE_ACCOUNT"
        },
        "privateEndpointConnections": [],
        "provisioningState": "Succeeded",
        "publicNetworkAccess": "Enabled"
    },
    "sku": {
        "capacity": 1,
        "name": "Standard"
    },
    "systemData": {
        "createdAt": "2022-02-23T09:46:46.2381767Z",
        "createdBy": "EMAIL@DOMAIN.COM",
        "createdByType": "User",
        "lastModifiedAt": "2022-02-23T09:46:46.2381767Z",
        "lastModifiedBy": "EMAIL@DOMAIN.COM",
        "lastModifiedByType": "User"
    },
    "tags": {},
    "type": "Microsoft.Purview/accounts"
}
```
</p>
</details>