# pv share createAsset

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  createAsset

## Description

Adds a new asset to an existing share.

## Syntax

```
pv share createAsset --sentShareName=<val> --assetName=<val> --payloadFile=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--assetName` (string)

The name of the asset.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Assets > [Create](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/assets/create)
```
PUT https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/assets/{assetName}
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
