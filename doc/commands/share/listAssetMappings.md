# pv share listAssetMappings

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listAssetMappings

## Description

List AssetMappings in a received share.

## Syntax

```
pv share listAssetMappings --receivedShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping

Share Data Plane > Asset Mappings > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/asset-mappings/list)
```
GET https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}/assetMappings
```

## Examples

Description
```powershell
pv share _EXAMPLE_
```


<details><summary>Sample response.</summary>
<p>

```json
{
    "key": "value"
}
```
</p>
</details>
