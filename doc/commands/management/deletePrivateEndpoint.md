# pv management deletePrivateEndpoint
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > deletePrivateEndpoint

## Description
Deletes private endpoint connection.

## Syntax
```
pv management deletePrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Private Endpoint Connections > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/delete)
```
DELETE https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName}
```

## Examples
```powershell

```