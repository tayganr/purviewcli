# pv management addRootCollectionAdmin
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > addRootCollectionAdmin

## Description
Add the administrator for root collection associated with this account.

## Syntax
```
pv management addRootCollectionAdmin --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --objectId=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account.

`--objectId` (string)  
The object identifier of the admin.

## Optional Arguments
*None*

## API Mapping
Accounts > [Add Root Collection Admin](https://docs.microsoft.com/en-us/rest/api/purview/accounts/add-root-collection-admin)
```
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/addRootCollectionAdmin
```

## Examples
Assign the collection administrator role to a user via their Azure AD object identifier at the root collection of the Azure Purview account.
```powershell
pv management addRootCollectionAdmin --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "myrg" --accountName "my-purview-account" --objectId "ac2b4099-7d5a-4d71-b9e4-65325a82c487"
```