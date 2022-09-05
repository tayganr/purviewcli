# pv share getAcceptedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  getAcceptedShare

## Description

Get an accepted share with acceptedSentShareName to a particular sent share.

## Syntax

```
pv share getAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val>
```

## Required Arguments

`--sentShareName` (string)

The name of the sent share.

`--acceptedSentShareName` (string)

The name of the accepted sent share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Accepted Sent Shares > [Get](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/accepted-sent-shares/get)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}
```

## Examples

Get an accepted share for a particular sent share.

```powershell
pv share getAcceptedShare --sentShareName "NewShare" --acceptedSentShareName "be2c3f1d-ac06-4aca-a5f8-28b44cad17ef"
```


<details><summary>Sample response.</summary>
<p>

```json
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
```
</p>
</details>
