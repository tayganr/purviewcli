# pv share createAssetMapping

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  createAssetMapping

## Description

Maps a source asset in the sent share to a destination asset in the received share.

## Syntax

```
pv share createAssetMapping --receivedShareName=<val> --assetMappingName=<val> --payloadFile=<val>
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

`--assetMappingName` (string)

The name of the asset mapping.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Asset Mappings > [Create](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/asset-mappings/create)
```
PUT https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}/assetMappings/{assetMappingName}
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
