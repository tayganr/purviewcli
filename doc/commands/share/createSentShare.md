# pv share createSentShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  createSentShare

## Description

Create a sent share in the given Purview account.

## Syntax

```
pv share createSentShare --sentShareName=<val> --payloadFile=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Sent Shares > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/create-or-update)
```
PUT https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
```

## Examples

Create a sent share.

```powershell
pv share createSentShare --sentShareName "MyNewSentShare" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
    "properties": {
        "description": "This is a friendly description.",
        "collection": {
            "referenceName": "pvdemo52dg4-pv",
            "type": "CollectionReference"
        }
    },
    "shareKind": "InPlace"
}
```
</p>
</details>
