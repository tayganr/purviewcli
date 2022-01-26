# pv management putPrivateEndpoint
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > putPrivateEndpoint

## Description
Approves/Rejects private endpoint connection request.

## Syntax
```
pv management putPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Private Endpoint Connections > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/create-or-update)
```
PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName}
```

## Examples
```powershell

```