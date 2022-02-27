# pv account updateAccount
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > updateAccount

## Description
Updates an account.

## Syntax
```
pv account updateAccount --friendlyName=<val>
```

## Required Arguments
`--friendlyName` (string)  
The friendly name of the account.

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Accounts > [Update Account Properties](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/accounts/update-account-properties)
```
PATCH https://{accountName}.purview.azure.com/account/
```

## Examples
Update the friendly name of the account.
```powershell
pv account updateAccount --friendlyName "Purview Sandbox"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/esg/providers/Microsoft.Purview/accounts/esg-26fa7f24-pv",
    "identity": {
        "principalId": "YOUR_PRINCIPAL_ID",
        "tenantId": "YOUR_TENANT_ID",
        "type": "SystemAssigned"
    },
    "location": "westeurope",
    "name": "esg-26fa7f24-pv",
    "properties": {
        "cloudConnectors": {
            "awsExternalId": "YOUR_AWS_EXTERNAL_ID"
        },
        "createdAt": "2022-02-23T09:46:46.2381767Z",
        "createdBy": "EMAIL@DOMAIN.com",
        "createdByObjectId": "AZURE_AD_OBJECT_ID",
        "endpoints": {
            "catalog": "https://esg-26fa7f24-pv.purview.azure.com/catalog",
            "guardian": "https://esg-26fa7f24-pv.purview.azure.com/guardian",
            "scan": "https://esg-26fa7f24-pv.purview.azure.com/scan"
        },
        "friendlyName": "My Azure Purview Account",
        "managedResourceGroupName": "managed-rg-esg-26fa7f24-pv",
        "managedResources": {
            "eventHubNamespace": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/managed-rg-esg-26fa7f24-pv/providers/Microsoft.EventHub/namespaces/YOUR_EVENT_HUB",
            "resourceGroup": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/managed-rg-esg-26fa7f24-pv",
            "storageAccount": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/managed-rg-esg-26fa7f24-pv/providers/Microsoft.Storage/storageAccounts/YOUR_STORAGE_ACCOUNT"
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
        "createdBy": "EMAIL@DOMAIN.com",
        "createdByType": "User",
        "lastModifiedAt": "2022-02-23T09:46:46.2381767Z",
        "lastModifiedBy": "EMAIL@DOMAIN.com",
        "lastModifiedByType": "User"
    },
    "tags": {},
    "type": "Microsoft.Purview/accounts"
}
```
</p>
</details>