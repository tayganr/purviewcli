# pv share listSentInvitations

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  listSentInvitations

## Description

List all Invitations in a share.

## Syntax

```
pv share listSentInvitations --sentShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
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

Share Data Plane > Sent Share Invitations > [List](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-share-invitations/list)
```
GET https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}/sentShareInvitations
```

## Examples

List all sent invitations for a sent share.

```powershell
pv share listSentInvitations --sentShareName "NewShare"
```


<details><summary>Sample response.</summary>
<p>

```json
{
   "value":[
      {
         "id":"/sentShares/NewShare/sentShareInvitations/607c8df07dc82107ccab50bd1b8c792279b1d9fc",
         "invitationKind":"User",
         "name":"607c8df07dc82107ccab50bd1b8c792279b1d9fc",
         "properties":{
            "invitationId":"47d63726-9373-417e-94a2-85afad2edd3e",
            "invitationStatus":"Pending",
            "provisioningState":"Succeeded",
            "senderEmail":"tarifat@microsoft.com",
            "senderName":"Taygan Rifat",
            "senderTenantName":"Microsoft",
            "sentAt":"2022-09-02T13:31:32.6057188Z",
            "shareKind":"InPlace",
            "targetEmail":"taygan.rifat@microsoft.com"
         },
         "type":"sentShares/sentShareInvitations"
      }
   ]
}
```
</p>
</details>
