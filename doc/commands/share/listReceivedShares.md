# pv share listReceivedShares

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listReceivedShares

## Description

Get a list of received shares.

## Syntax

```
pv share listReceivedShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--invitationName` (string)

Name of the invitation.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping

Share Data Plane > Received Shares > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-shares/list)
```
GET https://{accountName}.purview.azure.com/share/receivedShares
```

## Examples

Get a list of received shares.

```powershell
pv share listReceivedShares
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
      {
         "id":"/receivedShares/MyShare",
         "name":"MyShare",
         "properties":{
            "collection":{
               "referenceName":"djqn0b",
               "type":"CollectionReference"
            },
            "createdAt":"2022-09-01T08:14:47.7203367Z",
            "invitationId":"fb913088-56cd-40d3-abc5-fbae5597dbf8",
            "provisioningState":"Succeeded",
            "receivedShareStatus":"SourceDeleted",
            "receiverEmail":"tarifat@microsoft.com",
            "receiverName":"Taygan Rifat",
            "receiverTenantName":"Microsoft",
            "senderEmail":"tarifat@microsoft.com",
            "senderName":"Taygan Rifat",
            "senderTenantName":"Microsoft",
            "sentShareDescription":"",
            "sentShareLocation":"northeurope",
            "shareName":"MyShare",
            "sharedAt":"2022-09-01T08:14:30.3982663Z"
         },
         "shareKind":"InPlace",
         "type":"receivedShares"
      },
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
   ]
}
```
</p>
</details>
