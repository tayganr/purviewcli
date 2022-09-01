# pv share getSentShare
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > getSentShare

## Description
Deletes a sent share.

## Syntax
```
pv share deleteSentShare --sentShareName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > Sent Shares > [Delete](LINK)
```
DELETE https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
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
