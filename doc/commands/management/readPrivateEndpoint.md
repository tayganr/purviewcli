# pv management readPrivateEndpoint
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readPrivateEndpoint

## Description
Gets private endpoint connection information.

## Syntax
```
pv management readPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Private Endpoint Connections > Get > ](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/get)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName}
```

## Examples
```powershell

```