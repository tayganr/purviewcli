# pv management updateAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > updateAccount

## Description
Patches the account resource.

## Syntax
```
pv management updateAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Accounts > [Update](https://docs.microsoft.com/en-us/rest/api/purview/accounts/update)
```
PATCH https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
```powershell

```