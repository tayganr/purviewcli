# pv share listSentShares

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listSentShares

## Description

Get list of sent shares in the given Purview account.

## Syntax

```
pv share listSentShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--invitationName` (string)

Name of the invitation.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

`--filter` (string)

Filters the results using OData syntax.

`--orderBy` (string)

Sorts the results using OData syntax.

## API Mapping

Share Data Plane > Sent Shares > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares
```

## Examples

Get a list of sent shares.

```powershell
pv share listSentShares
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
      {
         "id":"/sentShares/NewShare",
         "name":"NewShare",
         "properties":{
            "collection":{
               "referenceName":"qrzdyx",
               "type":"CollectionReference"
            },
            "createdAt":"2022-09-01T16:48:25.0489591Z",
            "description":"This is a description.",
            "provisioningState":"Succeeded",
            "senderEmail":"tarifat@microsoft.com",
            "senderName":"Taygan Rifat",
            "senderTenantName":"Microsoft"
         },
         "shareKind":"InPlace",
         "type":"sentShares"
      }
   ]
}
```
</p>
</details>
