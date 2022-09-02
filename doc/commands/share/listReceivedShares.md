# pv share listReceivedShares

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listReceivedShares

## Description

Get a list of received shares.

## Syntax

```
pv share listReceivedShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--invitationName` (string)

Name of the invitation.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping

Share Data Plane > Received Shares > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-shares/list)
```
GET https://{accountName}.purview.azure.com/share/receivedShares
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
