# pv share getAsset

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getAsset

## Description

Get asset in a sentShare.

## Syntax

```
pv share getAsset --sentShareName=<val> --assetName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--assetName` (string)

The name of the asset.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Assets > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/assets/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/assets/{assetName}
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
