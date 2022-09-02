# pv share revokeAcceptedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  revokeAcceptedShare

## Description

Revoke an accepted sent share's access

## Syntax

```
pv share revokeAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--acceptedSentShareName` (string)

The name of the accepted sent share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Accepted Sent Shares > [Revoke](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/revoke)
```
POST https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}:revoke
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
