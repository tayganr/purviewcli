# pv share listAcceptedShares

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listAcceptedShares

## Description

List of accepted shares for the current sent share.

## Syntax

```
pv share listAcceptedShares --sentShareName=<val> [--skipToken=<val>]
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

## API Mapping

Share Data Plane > Accepted Sent Shares > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares
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
