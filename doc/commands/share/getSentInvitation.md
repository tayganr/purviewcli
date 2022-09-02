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

Description
```powershell
pv share _EXAMPLE_
```


<details><summary>Sample response.</summary>
<p>

```json
{
    "key": "value"
}
```
</p>
</details>
