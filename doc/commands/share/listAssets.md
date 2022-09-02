# pv share listAssets

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listAssets

## Description

List Assets in a share.

## Syntax

```
pv share listAssets --sentShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping
Share Data Plane > Assets > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/assets/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/assets
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
