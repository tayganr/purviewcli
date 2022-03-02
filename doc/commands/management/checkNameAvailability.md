# pv management checkNameAvailability
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > checkNameAvailability

## Description
Checks the account name availability.

## Syntax
```
pv management checkNameAvailability --subscriptionId=<val> --accountName=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--accountName` (string)  
The name of the account.

## Optional Arguments
*None*

## API Mapping
Accounts > [Check Name Availability](https://docs.microsoft.com/en-us/rest/api/purview/accounts/check-name-availability)
```
POST https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Purview/checkNameAvailability
```

## Examples
Check if the account name is available.
```powershell
pv management checkNameAvailability --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --accountName "my-new-purview-account-name"
```

<details><summary>Sample response.</summary>
<p>

```json
{    
    "nameAvailable": true
}
```
</p>
</details>