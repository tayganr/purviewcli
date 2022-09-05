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

Update the expiration date of an accepted share.

```powershell
pv share updateExpirationAcceptedShare --sentShareName "MyNewSentShare" --acceptedSentShareName "4f5e1b4b-44f8-42c1-a783-b6c2265e49f5" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
    "shareKind": "InPlace",
    "properties": {
        "expirationDate": "2023-02-24T21:02:24.695Z"
    }
}
```
</p>
</details>
