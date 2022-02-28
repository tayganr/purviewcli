# pv management deleteAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > deleteAccount

## Description
Deletes the account resource.

## Syntax
```
pv management deleteAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account.

## Optional Arguments
*None*

## API Mapping
Accounts > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/accounts/delete)
```
DELETE https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
```powershell
pv management deleteAccount --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg" --accountName "esg-26fa7f24-pv"
```