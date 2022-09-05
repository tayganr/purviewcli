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

Get asset from a sent share.

```powershell
pv share getAsset --sentShareName "NewShare" --assetName "assetName"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "id":"/sentShares/NewShare/assets/assetName",
   "kind":"BlobAccount",
   "name":"assetName",
   "properties":{
      "location":"uksouth",
      "paths":[
         {
            "containerName":"products",
            "receiverPath":"products.csv",
            "senderPath":"products.csv"
         }
      ],
      "provisioningState":"Succeeded",
      "receiverAssetName":"assetName",
      "storageAccountResourceId":"/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pv-7643-rg/providers/Microsoft.Storage/storageAccounts/storagedatashare01"
   },
   "type":"sentShares/assets"
}
```
</p>
</details>
