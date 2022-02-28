# pv management setDefaultAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > setDefaultAccount

## Description
Sets the default account for the scope.

## Syntax
```
pv management setDefaultAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --scopeTenantId=<val> --scopeType=<val> --scope=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account.

`--scopeTenantId` (string)  
The tenant ID.

`--scopeType` (string)  
The scope for the default account (Subscription OR Tenant).

`--scope` (string)  
The Id of the scope object, for example if the scope is "Subscription" then it is the ID of that subscription.

## Optional Arguments
*None*

## API Mapping
Default Accounts > [Set](https://docs.microsoft.com/en-us/rest/api/purview/default-accounts/set)
```
POST https://management.azure.com/providers/Microsoft.Purview/setDefaultAccount
```

## Examples
```powershell
pv management setDefaultAccount --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg" --accountName "esg-26fa7f24-pv" --scopeTenantId "72f988bf-86f1-41af-91ab-2d7cd011db47" --scopeType "Subscription" --scope "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
```