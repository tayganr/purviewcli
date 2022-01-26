# pv management readAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readAccount

## Description
Gets the account resource.

## Syntax
```
pv management readAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Accounts > [Get](https://docs.microsoft.com/en-us/rest/api/purview/accounts/get)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
```powershell

```