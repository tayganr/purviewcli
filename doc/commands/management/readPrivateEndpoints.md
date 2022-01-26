# pv management readPrivateEndpoints
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > readPrivateEndpoints

## Description
Gets private endpoint connections.

## Syntax
```
pv management readPrivateEndpoints --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Private Endpoint Connections > [List By Account](https://docs.microsoft.com/en-us/rest/api/purview/private-endpoint-connections/list-by-account)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections
```

## Examples
```powershell

```