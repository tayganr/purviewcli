# pv share createSentInvitation

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  createSentInvitation

## Description

Create/Update a sent share invitation in the given account.

## Syntax

```
pv share createSentInvitation --sentShareName=<val> --invitationName=<val> --payloadFile=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--invitationName` (string)

Name of the invitation.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Sent Share Invitations > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-share-invitations/create-or-update)
```
PUT https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/sentShareInvitations/{sentShareInvitationName}
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
