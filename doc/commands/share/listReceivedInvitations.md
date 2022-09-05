# pv share listReceivedInvitations

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listReceivedInvitations

## Description

Lists received invitations.

## Syntax

```
pv share listReceivedInvitations [--skipToken=<val> --filter=<val> --orderBy=<val>]
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

Share Data Plane > Received Invitations > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-invitations/list)
```
GET https://{accountName}.purview.azure.com/share/receivedInvitations
```

## Examples

Get a list of received invitations.

```powershell
pv share listReceivedInvitations
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
      {
         "id":"/receivedInvitations/0acdde01-bdbd-49e1-b3d8-275d62b9b9bc",
         "invitationKind":"User",
         "name":"0acdde01-bdbd-49e1-b3d8-275d62b9b9bc",
         "properties":{
            "description":"This is a description.",
            "invitationStatus":"Pending",
            "location":"northeurope",
            "receiverEmail":"tarifat@microsoft.com",
            "receiverName":null,
            "receiverTenantName":null,
            "senderEmail":"tarifat@microsoft.com",
            "senderName":"Taygan Rifat",
            "senderTenantName":"Microsoft",
            "sentAt":"2022-09-02T13:38:29.3185176Z",
            "sentShareName":"NewShare",
            "shareKind":"InPlace",
            "targetEmail":"tarifat@microsoft.com"
         },
         "type":"receivedInvitations"
      }
   ]
}
```
</p>
</details>
