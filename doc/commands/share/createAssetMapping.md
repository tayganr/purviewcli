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

Delete an asset mapping for a particular received share.

```powershell
pv share createAssetMapping --receivedShareName "MyNewReceivedShare" --assetMappingName "MyAssetMappingName" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
  "kind": "BlobAccount",
  "properties": {
    "assetId": "8c3538ba-e787-4823-83ab-f01de6c18289",
    "storageAccountResourceId": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pv-7643-rg/providers/Microsoft.Storage/storageAccounts/storagedatashare01",
    "containerName": "customer",
    "folder": "helloWorld",
    "mountPath": ""
  }
}
```
</p>
</details>
