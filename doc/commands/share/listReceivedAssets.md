# pv share listReceivedAssets

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listReceivedAssets

## Description

List source asset of a received share.

## Syntax

```
pv share listReceivedAssets --receivedShareName=<val> [--skipToken=<val>]
```

## Required Arguments

`--receivedShareName` (string)

The name of the received share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

## API Mapping

Share Data Plane > Received Assets > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-assets/list)
```
GET https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}/receivedAssets
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
