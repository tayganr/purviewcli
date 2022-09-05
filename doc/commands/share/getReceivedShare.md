# pv share getReceivedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getReceivedShare

## Description

Get a received share by name.

## Syntax

```
pv share getReceivedShare --receivedShareName=<val>
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Received Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-shares/get)
```
GET https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}
```

## Examples

Get a received share.

```powershell
pv share getReceivedShare --receivedShareName "NewShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "id":"/receivedShares/NewShare",
   "name":"NewShare",
   "properties":{
      "collection":{
         "referenceName":"pvdemo52dg4-pv",
         "type":"CollectionReference"
      },
      "createdAt":"2022-09-02T13:28:13.1922869Z",
      "invitationId":"037ac95e-98a4-4b6a-aba7-7f915ab72497",
      "provisioningState":"Succeeded",
      "receivedShareStatus":"Active",
      "receiverEmail":"tarifat@microsoft.com",
      "receiverName":"Taygan Rifat",
      "receiverTenantName":"Microsoft",
      "senderEmail":"tarifat@microsoft.com",
      "senderName":"Taygan Rifat",
      "senderTenantName":"Microsoft",
      "sentShareDescription":"This is a description.",
      "sentShareLocation":"northeurope",
      "shareName":"NewShare",
      "sharedAt":"2022-09-01T16:48:25.7585096Z"
   },
   "shareKind":"InPlace",
   "type":"receivedShares"
}
```
</p>
</details>
