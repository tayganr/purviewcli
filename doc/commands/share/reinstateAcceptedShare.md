# pv share reinstateAcceptedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  reinstateAcceptedShare

## Description

Reinstate a revoked accepted sent share.

## Syntax

```
pv share reinstateAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val> --payloadFile=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--acceptedSentShareName` (string)

The name of the accepted sent share.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Accepted Sent Shares > [Reinstate](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/reinstate)
```
POST https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}:reinstate
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
