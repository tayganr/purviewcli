# pv management createAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > createAccount

## Description
Create or update an account resource

## Syntax
```
pv management createAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Accounts > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/accounts/create-or-update)
```
PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
```powershell

```