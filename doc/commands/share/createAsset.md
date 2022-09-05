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

Add an asset to an existing sent share.

```powershell
pv share createAsset --sentShareName "MyNewSentShare" --assetName "MyAssetName" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
    "kind": "BlobAccount",
    "properties": {
        "storageAccountResourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pv-7643-rg/providers/Microsoft.Storage/storageAccounts/storagedatashare01",
        "receiverAssetName": "MyAssetName",
        "paths": [
            {
                "containerName": "products",
                "senderPath": "products.csv",
                "receiverPath": "products.csv"
            }
        ]
    }
}
```
</p>
</details>
