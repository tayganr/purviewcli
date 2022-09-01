# pv share _COMMAND_
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > _COMMAND_

## Description
_DESCRIPTION_

## Syntax
```
pv share _COMMAND__ARGS_
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > H2 > [H3](LINK)
```
METHOD https://{accountName}.purview.azure.com/share/endpoint
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
   "name":"assetName",
   "type":"Microsoft.Purview/Share/assets",
   "id":"",
   "kind":"BlobAccount",
   "properties":{
      "storageAccountResourceId":"/subscriptions/YOUR_AZURE_SUBSCRIPTION_ID/resourceGroups/YOUR_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/YOUR_STORAGE_ACCOUNT",
      "receiverAssetName":"assetName",
      "paths":[
         {
            "containerName":"products",
            "senderPath":"products.csv",
            "receiverPath":"products.csv"
         }
      ]
   }
}
```
</p>
</details>
