# pv management defaultAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > defaultAccount

## Description
Gets the default account information set for the scope.

## Syntax
```
pv management defaultAccount --scopeTenantId=<val> --scopeType=<val> --scope=<val>
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
Default Accounts > [Get](https://docs.microsoft.com/en-us/rest/api/purview/default-accounts/get)
```
GET https://management.azure.com/providers/Microsoft.Purview/getDefaultAccount
```

## Examples
```powershell
pv management defaultAccount --scopeTenantId "72f988bf-86f1-41af-91ab-2d7cd011db47" --scopeType "Subscription" --scope "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
```