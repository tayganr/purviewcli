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

Get a list of asset mappings for a particular received share.

```powershell
pv share listAssetMappings --receivedShareName "MyShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
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
   ]
}
```
</p>
</details>
