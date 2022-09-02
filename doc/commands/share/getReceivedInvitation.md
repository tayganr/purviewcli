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
