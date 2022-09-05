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

Create a sent invitation from a sent share.

```powershell
pv share createSentInvitation --sentShareName "MyNewSentShare" --invitationName "650f1292-9c84-44c9-9339-342b88940dbc" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
    "invitationKind": "User",
    "properties": {
        "targetActiveDirectoryId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
        "targetObjectId": "095354ff-cae8-44ff-8120-22ec5a941b40",
        "targetEmail": "tarifat@microsoft.com"
    }
}
```
</p>
</details>
