# pv share getReceivedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getReceivedShare

## Description

Get a received share by name.

## Syntax

```
pv share getReceivedShare --receivedShareName=<val>
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Received Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-shares/get)
```
GET https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}
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
