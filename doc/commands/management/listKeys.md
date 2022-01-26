# pv management listKeys
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > listKeys

## Description
Lists the keys asynchronous.

## Syntax
```
pv management listKeys --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Accounts > List Keys > ](https://docs.microsoft.com/en-us/rest/api/purview/accounts/list-keys)
```
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/listkeys
```

## Examples
```powershell

```