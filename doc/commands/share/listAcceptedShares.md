# pv share listAcceptedShares

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listAcceptedShares

## Description

List of accepted shares for the current sent share.

## Syntax

```
pv share listAcceptedShares --sentShareName=<val> [--skipToken=<val>]
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

## Optional Arguments

`--skipToken` (string)

The continuation token to list the next page.

## API Mapping

Share Data Plane > Accepted Sent Shares > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares
```

## Examples

List accepted shares for a particular sent share.

```powershell
pv share listAcceptedShares --sentShareName "NewShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
      {
         "id":"/sentShares/NewShare/acceptedSentShares/be2c3f1d-ac06-4aca-a5f8-28b44cad17ef",
         "name":"be2c3f1d-ac06-4aca-a5f8-28b44cad17ef",
         "properties":{
            "createdAt":"2022-09-02T13:28:13.1922869Z",
            "expirationDate":null,
            "receivedShareStatus":"Active",
            "receiverEmail":"tarifat@microsoft.com",
            "receiverName":"Taygan Rifat",
            "receiverTargetObjectId":"095354ff-cae8-44ff-8120-22ec5a941b40",
            "receiverTenantName":"Microsoft",
            "senderEmail":"tarifat@microsoft.com",
            "senderName":"Taygan Rifat",
            "senderTenantName":"Microsoft",
            "sharedAt":"2022-09-01T16:48:25.7585096Z"
         },
         "shareKind":"InPlace",
         "type":"sentShares/acceptedSentShares"
      }
   ]
}
```
</p>
</details>
