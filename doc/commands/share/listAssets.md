# pv share listAssets

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listAssets

## Description

List Assets in a share.

## Syntax

```
pv share listAssets --sentShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping

Share Data Plane > Assets > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/assets/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/assets
```

## Examples

List assets in a sent share.

```powershell
pv share listAssets --sentShareName "NewShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
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
   ]
}
```
</p>
</details>
