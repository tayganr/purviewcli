# pv management addRootCollectionAdmin
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > addRootCollectionAdmin

## Description
Add the administrator for root collection associated with this account.

## Syntax
```
pv management addRootCollectionAdmin --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --objectId=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Accounts > [Add Root Collection Admin](https://docs.microsoft.com/en-us/rest/api/purview/accounts/add-root-collection-admin)
```
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/addRootCollectionAdmin
```

## Examples
```powershell

```