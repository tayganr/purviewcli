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

Accept a sent share by creating a received share.

```powershell
pv share createReceivedShare --receivedShareName "MyNewReceivedShare" --payloadFile "/path/to/file.json"
```


<details><summary>Example payload.</summary>
<p>

```json
{
    "properties": {
        "sentShareLocation": "northeurope",
        "invitationId": "71d43cbe-5e44-40a5-b747-4140752fce62",
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
