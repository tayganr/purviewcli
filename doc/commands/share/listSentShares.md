# pv share listSentShares

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listSentShares

## Description

Get list of sent shares in the given Purview account.

## Syntax

```
pv share listSentShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--invitationName` (string)

Name of the invitation.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping

Share Data Plane > Sent Shares > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares
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
