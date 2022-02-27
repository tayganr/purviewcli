# pv account putCollection
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > putCollection

## Description
Creates or updates a collection entity.

## Syntax
```
pv account putCollection --friendlyName=<val> --parentCollection=<val>
```

## Required Arguments
`--friendlyName` (string)  
The friendly name of the collection.

`--parentCollection` (string)  
This is the unique name of the parent collection (not the friendly name).

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Collections > [Create Or Update Collection](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/collections/create-or-update-collection)
```
PUT https://{accountName}.purview.azure.com/account/collections/{collectionName}
```

## Examples
Create or update a collection.
```powershell
pv account putCollection --friendlyName "hello world" --parentCollection "w0kfma"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "collectionProvisioningState": "Succeeded",
    "friendlyName": "hello world",
    "name": "qW48hl",
    "parentCollection": {
        "referenceName": "w0kfma",
        "type": "CollectionReference"
    },
    "systemData": {
        "createdAt": "2022-02-27T13:04:36.9095861Z",
        "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
        "createdByType": "User",
        "lastModifiedAt": "2022-02-27T13:04:36.9095862Z",
        "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
        "lastModifiedByType": "User"
    }
}
```
</p>
</details>