# pv share deleteSentInvitation

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  deleteSentInvitation

## Description

Delete Invitation in a share.

## Syntax

```
pv share deleteSentInvitation --sentShareName=<val> --invitationName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--invitationName` (string)

Name of the invitation.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Sent Share Invitations > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-share-invitations/delete)
```
DELETE https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/sentShareInvitations/{sentShareInvitationName}
```

## Examples

Delete a sent invitation for a sent share.

```powershell
pv share deleteSentInvitation --sentShareName "NewShare" --invitationName "7543515465d5676285972198ef4cdc1dd3a0f711"
```