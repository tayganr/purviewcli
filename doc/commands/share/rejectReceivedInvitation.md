# pv share rejectReceivedInvitation

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  rejectReceivedInvitation

## Description

Rejects the received invitation identified by name

## Syntax

```
pv share rejectReceivedInvitation --invitationName=<val> --payloadFile=<val>
```

## Required Arguments

`--invitationName` (string)

Name of the invitation.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Received Invitations > [Reject](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-invitations/reject)
```
POST https://{accountName}.purview.azure.com/share/receivedInvitations/{receivedInvitationName}:reject
```

## Examples

Reject a received invitation.

```powershell
pv share rejectReceivedInvitation --invitationName "955af42b-b08d-4a00-ba58-aaf31afcd53a" --payloadFile "/path/to/file.json"
```


<details><summary>Sample response.</summary>
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
