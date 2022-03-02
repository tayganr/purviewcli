# pv management readPrivateEndpoints
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readPrivateEndpoints

## Description
Gets private endpoint connections.

## Syntax
```
pv management readPrivateEndpoints --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account

## Optional Arguments
*None*

## API Mapping
Private Endpoint Connections > [List By Account](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/list-by-account)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections
```

## Examples
Get information on private endpoint connections.
```powershell
pv management readPrivateEndpoints --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "private" --accountName "taygan-private-pv"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 1,
    "value": [
        {
            "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/private/providers/Microsoft.Purview/accounts/taygan-private-pv/privateEndpointConnections/purview-pe-instance-a2dbee21-876d-43a4-b521-df9863a98553",
            "name": "purview-pe-instance-a2dbee21-876d-43a4-b521-df9863a98553",
            "properties": {
                "privateEndpoint": {
                    "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/private/providers/Microsoft.Network/privateEndpoints/purview-pe-instance"
                },
                "privateLinkServiceConnectionState": {
                    "actionsRequired": "None",
                    "status": "Approved"
                },
                "provisioningState": "Succeeded"
            },
            "type": "Microsoft.Purview/accounts/privateEndpointConnections"
        }
    ]
}
```
</p>
</details>