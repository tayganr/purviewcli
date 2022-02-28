# pv management readAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readAccount

## Description
Gets the account resource.

## Syntax
```
pv management readAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
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
Accounts > [Get](https://docs.microsoft.com/en-us/rest/api/purview/accounts/get)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
Get the properties of an existing Azure Purview account.
```powershell
pv management readAccount --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg" --accountName "esg-26fa7f24-pv"
```

<details><summary>Sample response.</summary>
<p>

```json

```
</p>
</details>