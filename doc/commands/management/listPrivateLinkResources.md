# pv management listPrivateLinkResources
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > listPrivateLinkResources

## Description
Gets a list of privately linkable resources for an account

## Syntax
```
pv management listPrivateLinkResources --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> [--groupId=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Private Link Resources > [List By Account](https://docs.microsoft.com/en-us/rest/api/purview/private-link-resources/list-by-account)
```
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateLinkResources
```

## Examples
```powershell

```