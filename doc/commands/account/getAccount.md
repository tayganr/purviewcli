# pv account getAccount
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getAccount

## Description
Get an account.

## Syntax
```
pv account getAccount
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Accounts > [Get Account Properties](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/accounts/get-account-properties)
```
GET https://{accountName}.purview.azure.com/account/
```

## Examples
Get account properties.
```powershell
pv account getAccount
```