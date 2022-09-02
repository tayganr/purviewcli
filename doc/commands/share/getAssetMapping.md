# pv share getAssetMapping

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getAssetMapping

## Description

Get AssetMapping in a receivedShare.

## Syntax

```
pv share getAssetMapping --receivedShareName=<val> --assetMappingName=<val>
```

## Required Arguments

`--receivedShareName` (string)
The name of the received share.

`--assetMappingName` (string)
The name of the asset mapping.

## Optional Arguments

*None*

## API Mapping
Share Data Plane > Asset Mappings > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/asset-mappings/get)
```
GET https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}/assetMappings/{assetMappingName}
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
