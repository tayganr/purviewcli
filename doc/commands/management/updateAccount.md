# pv management updateAccount
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > updateAccount

## Description
Patches the account resource.

## Syntax
```
pv management updateAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payloadFile=<val>
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
Accounts > [Update](https://docs.microsoft.com/en-us/rest/api/purview/accounts/update)
```
PATCH https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}
```

## Examples
Add a new tag to an existing Azure Purview account.
```powershell
pv management updateAccount --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg" --accountName "my-purview-account" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "tags": {
        "newTag": "New tag value."
    }
}
```
</p>
</details>