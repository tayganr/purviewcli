# pv share createReceivedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  createReceivedShare

## Description

Create a received share in the given account.

## Syntax

```
pv share createReceivedShare --receivedShareName=<val> --payloadFile=<val>
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Received Shares > [Create](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-shares/create)
```
PUT https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}
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
