# pv share listSentShares
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > listSentShares

## Description
Get list of sent shares in the given Purview account.

## Syntax
```
pv share listSentShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > Sent Shares > [List](LINK)
```
GET https://{accountName}.purview.azure.com/share/sentShares
```

## Examples
List all sent shares in a given Microsoft Purview account.
```powershell
pv share listSentShares
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "value": [
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
    ]
}
```
</p>
</details>
