# pv share _COMMAND_
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > _COMMAND_

## Description
Get a sent share in the given Purview account.

## Syntax
```
pv share getSentShare --sentShareName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > Sent Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
```

## Examples
Get a sent share in the given Microsoft Purview account by specifying the share name.
```powershell
pv share getSentShare --sentShareName "MyShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "/sentShares/MyShare",
    "name": "MyShare",
    "properties": {
        "collection": {
            "referenceName": "djqn0b",
            "type": "CollectionReference"
        },
        "createdAt": "2022-09-01T08:12:48.408025Z",
        "description": "",
        "provisioningState": "Succeeded",
        "senderEmail": "tarifat@microsoft.com",
        "senderName": "Taygan Rifat",
        "senderTenantName": "Microsoft"
    },
    "shareKind": "InPlace",
    "type": "sentShares"
}
```
</p>
</details>
