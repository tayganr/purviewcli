# pv management removeDefaultAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > removeDefaultAccount

## Description
Removes the default account from the scope.

## Syntax
```
pv management removeDefaultAccount --scopeTenantId=<val> --scopeType=<val> --scope=<val>
```

## Required Arguments
`--scopeTenantId` (string)  
The tenant ID.

`--scopeType` (string)  
The scope for the default account (Subscription OR Tenant).

`--scope` (string)  
The Id of the scope object, for example if the scope is "Subscription" then it is the ID of that subscription.

## Optional Arguments
*None*

## API Mapping
Default Accounts > [Remove](https://docs.microsoft.com/en-us/rest/api/purview/default-accounts/remove)
```
POST https://management.azure.com/providers/Microsoft.Purview/removeDefaultAccount
```

## Examples
```powershell

```