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
