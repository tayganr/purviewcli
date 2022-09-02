# pv share getAcceptedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getAcceptedShare

## Description

Get an accepted share with acceptedSentShareName to a particular sent share.

## Syntax

```
pv share getAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--acceptedSentShareName` (string)

The name of the accepted sent share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Accepted Sent Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}
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
