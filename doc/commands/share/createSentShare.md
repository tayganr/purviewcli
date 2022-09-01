# pv share createSentShare
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > createSentShare

## Description
Create a sent share in the given Purview account.

## Syntax
```
pv share createSentShare --sentShareName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > Sent Shares > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/create-or-update)
```
PUT https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
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
