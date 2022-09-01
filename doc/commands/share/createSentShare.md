# pv share createSentShare
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > createSentShare

## Description
Create a sent share in the given Purview account.

## Syntax
```
pv share createSentShare --sentShareName=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > Sent Shares > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/create-or-update)
```
PUT https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
```

## Examples
Description
```powershell
pv share createSentShare --sentShareName "NewShare" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
   "shareKind":"InPlace",
   "properties":{
      "description":"This is a description.",
      "collection":{
         "referenceName":"qrzdyx",
         "type":"CollectionReference"
      }
   }
}
```
</p>
</details>
