# pv management deleteAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > deleteAccount

## Description
Deletes the account resource.

## Syntax
```
pv management deleteAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Accounts > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/accounts/delete)
```
DELETE https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
```powershell

```