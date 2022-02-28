# pv management readAccounts
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readAccounts

## Description
Gets the accounts resources by subscription.

## Syntax
```
pv management readAccounts --subscriptionId=<val> [--resourceGroupName=<val>]
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

## Optional Arguments
`--resourceGroupName` (string)  
The resource group name.

## API Mapping
Accounts > [List By Subscription](https://docs.microsoft.com/en-us/rest/api/purview/accounts/list-by-subscription)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Purview/accounts
```

## Examples
Get all Azure Purview accounts within a particular Azure subscription.
```powershell
pv management readAccounts --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0"
```

<details><summary>Sample response.</summary>
<p>

```json

```
</p>
</details><br />

Get all Azure Purview accounts within a particular resource group.
```powershell
pv management readAccounts --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "esg"
```

<details><summary>Sample response.</summary>
<p>

```json

```
</p>
</details>