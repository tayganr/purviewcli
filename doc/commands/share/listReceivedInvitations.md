# pv share listReceivedInvitations

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listReceivedInvitations

## Description

Lists the received invitations.

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
