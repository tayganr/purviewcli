# pv share getSentShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getSentShare

## Description

Get a sent share in the given Purview account.

## Syntax

```
pv share getSentShare --sentShareName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Sent Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
```

## Examples

Get a sent share.

```powershell
pv share getSentShare --sentShareName "NewShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "id":"/sentShares/NewShare",
   "name":"NewShare",
   "properties":{
      "collection":{
         "referenceName":"qrzdyx",
         "type":"CollectionReference"
      },
      "createdAt":"2022-09-01T16:48:25.0489591Z",
      "description":"This is a description.",
      "provisioningState":"Succeeded",
      "senderEmail":"tarifat@microsoft.com",
      "senderName":"Taygan Rifat",
      "senderTenantName":"Microsoft"
   },
   "shareKind":"InPlace",
   "type":"sentShares"
}
```
</p>
</details>
