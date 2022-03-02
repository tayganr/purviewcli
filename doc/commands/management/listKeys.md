# pv management listKeys
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > listKeys

## Description
Lists the keys asynchronous.

## Syntax
```
pv management listKeys --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
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
Accounts > [List Keys](https://docs.microsoft.com/en-us/rest/api/purview/accounts/list-keys)
```
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/listkeys
```

## Examples
List the keys associated to an existing Azure Purview account.
```powershell
pv management listKeys --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "myrg" --accountName "my-purview-account"
```

<details><summary>Sample response.</summary>
<p>

```json
{  
    "atlasKafkaPrimaryEndpoint": "Endpoint=sb://ATLAS_ENDPOINT.servicebus.windows.net/;SharedAccessKeyName=AlternateSharedAccessKey;SharedAccessKey=YOUR_SHARED_ACCESS_KEY",
    "atlasKafkaSecondaryEndpoint": "Endpoint=sb://ATLAS_ENDPOINT.servicebus.windows.net/;SharedAccessKeyName=AlternateSharedAccessKey;SharedAccessKey=YOUR_SHARED_ACCESS_KEY"
}
```
</p>
</details>