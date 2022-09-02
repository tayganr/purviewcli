# pv share deleteAsset

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  deleteAsset

## Description

Delete asset in a sentShare.

## Syntax

```
pv share deleteAsset --sentShareName=<val> --assetName=<val>
```

## Required Arguments

`--sentShareName` (string)
The name of the sent share.

`--assetName` (string)
The name of the asset.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Assets > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/assets/delete)
```
DELETE https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/assets/{assetName}
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
