# pv share updateExpirationAcceptedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  updateExpirationAcceptedShare

## Description

Update the expiration date of an active accepted sent share.

## Syntax

```
pv share updateExpirationAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val> --payloadFile=<val>
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

Share Data Plane > Accepted Sent Shares > [Update Expiration](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/update-expiration)
```
POST https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}:update-expiration
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
