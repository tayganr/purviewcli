# pv share getSentInvitation

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getSentInvitation

## Description

Get Invitation for a given share.

## Syntax

```
pv share getSentInvitation --sentShareName=<val> --invitationName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--invitationName` (string)

Name of the invitation.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Sent Share Invitations > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-share-invitations/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/sentShareInvitations/{sentShareInvitationName}
```

## Examples

Get a sent invitation for a sent share.

```powershell
pv share getSentInvitation --sentShareName "NewShare" --invitationName "607c8df07dc82107ccab50bd1b8c792279b1d9fc"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "id":"/sentShares/NewShare/sentShareInvitations/607c8df07dc82107ccab50bd1b8c792279b1d9fc",
   "invitationKind":"User",
   "name":"607c8df07dc82107ccab50bd1b8c792279b1d9fc",
   "properties":{
      "invitationId":"47d63726-9373-417e-94a2-85afad2edd3e",
      "invitationStatus":"Pending",
      "provisioningState":"Succeeded",
      "senderEmail":"tarifat@microsoft.com",
      "senderName":"Taygan Rifat",
      "senderTenantName":"Microsoft",
      "sentAt":"2022-09-02T13:31:32.6057188Z",
      "shareKind":"InPlace",
      "targetEmail":"taygan.rifat@microsoft.com"
   },
   "type":"sentShares/sentShareInvitations"
}
```
</p>
</details>
