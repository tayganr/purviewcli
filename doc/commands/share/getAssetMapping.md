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

Get an asset mapping for a particular received share.

```powershell
pv share getAssetMapping --receivedShareName "MyShare" --assetMappingName "storagedatashare01"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "id":"/receivedShares/MyShare/assetMappings/storagedatashare01",
   "kind":"BlobAccount",
   "name":"storagedatashare01",
   "properties":{
      "assetId":"f4a4d0f9-d3db-4c80-944e-fe692705f27f",
      "assetMappingStatus":"Broken",
      "containerName":"customer",
      "folder":"helloWorld",
      "location":"uksouth",
      "mountPath":"",
      "provisioningState":"Succeeded",
      "storageAccountResourceId":"/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pv-7643-rg/providers/Microsoft.Storage/storageAccounts/storagedatashare01"
   },
   "type":"receivedShares/assetMappings"
}
```
</p>
</details>
