# pv account updateAccount
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > updateAccount

## Description
Updates an account.

## Syntax
```
pv account updateAccount --friendlyName=<val>
```

## Required Arguments
`--friendlyName` (string)  
The friendly name of the account.

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Accounts > [Update Account Properties](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/accounts/update-account-properties)
```
PATCH https://{accountName}.purview.azure.com/account/
```

## Examples
Update the friendly name of the account.
```powershell
pv account updateAccount --friendlyName "Purview Sandbox"
```