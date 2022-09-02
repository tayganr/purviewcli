# pv share getSentShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getSentShare

## Description

Get a sent share in the given Purview account.

## Syntax

```
pv share getSentShare --sentShareName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Sent Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
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
