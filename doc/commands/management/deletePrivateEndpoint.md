# pv management deletePrivateEndpoint
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > deletePrivateEndpoint

## Description
Deletes private endpoint connection.

## Syntax
```
pv management deletePrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
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
Private Endpoint Connections > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/delete)
```
DELETE https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName}
```

## Examples
Delete a private endpoint.
```powershell
pv management deletePrivateEndpoint --subscriptionId "2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0" --resourceGroupName "private" --accountName "taygan-private-pv" --privateEndpointConnectionName "purview-pe-instance-a2dbee21-876d-43a4-b521-df9863a98553"
```