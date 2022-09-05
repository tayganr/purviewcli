# pv share listReceivedAssets

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listReceivedAssets

## Description

List source asset of a received share.

## Syntax

```
pv share listReceivedAssets --receivedShareName=<val> [--skipToken=<val>]
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

## API Mapping

Share Data Plane > Received Assets > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-assets/list)
```
GET https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}/receivedAssets
```

## Examples

Get a list of received assets from a particular received share.

```powershell
pv share listReceivedAssets --receivedShareName "NewShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
      {
         "id":"/receivedShares/NewShare/receivedAssets/6408e9cb-273a-49c7-8e2d-c89e928fd197",
         "kind":"BlobAccount",
         "name":"6408e9cb-273a-49c7-8e2d-c89e928fd197",
         "properties":{
            "location":"uksouth",
            "receiverAssetName":"assetName",
            "receiverPaths":[
               "products.csv"
            ]
         },
         "type":"receivedShares/receivedAssets"
      }
   ]
}
```
</p>
</details>
