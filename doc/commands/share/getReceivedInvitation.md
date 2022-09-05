# pv share getReceivedInvitation

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getReceivedInvitation

## Description

Gets the received invitation identified by name.

## Syntax

```
pv share getReceivedInvitation --invitationName=<val>
```

## Required Arguments

`--invitationName` (string)

Name of the invitation.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Received Invitations > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-invitations/get)
```
GET https://{accountName}.purview.azure.com/share/receivedInvitations/{receivedInvitationName}
```

## Examples

Get a received invitation.

```powershell
pv share getReceivedInvitation --invitationName "0acdde01-bdbd-49e1-b3d8-275d62b9b9bc"
```


<details><summary>Sample response.</summary>
<p>

```json
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
```
</p>
</details>
