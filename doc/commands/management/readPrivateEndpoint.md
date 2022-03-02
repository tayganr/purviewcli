# pv management readPrivateEndpoint
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readPrivateEndpoint

## Description
Gets private endpoint connection information.

## Syntax
```
pv management readPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
```

## Required Arguments
`--subscriptionId` (string)  
The subscription identifier.

`--resourceGroupName` (string)  
The resource group name.

`--accountName` (string)  
The name of the account

`--privateEndpointConnectionName` (string)  
Name of the private endpoint connection.

## Optional Arguments
*None*

## API Mapping
Private Endpoint Connections > [Get](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/get)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName}
```

## Examples
Get information on a private endpoint connection.
```powershell
pv management readPrivateEndpoint --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "private" --accountName "taygan-private-pv" --privateEndpointConnectionName "purview-pe-instance-a2dbee21-876d-43a4-b521-df9863a98553"
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