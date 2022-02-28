# pv management createAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > createAccount

## Description
Create or update an account resource

## Syntax
```
pv management createAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payloadFile=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Accounts > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/accounts/create-or-update)
```
PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
```powershell
pv management createAccount --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "synapse" --accountName "taygan-26fa7f24-pv" --payloadFile "/path/to/file.json"
```