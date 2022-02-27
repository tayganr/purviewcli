# pv account getCollection
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getCollection

## Description
Get a collection.

## Syntax
```
pv account getCollection --collectionName=<val>
```

## Required Arguments
`--collectionName` (string)  
This is the unique name of the collection (not the friendly name).

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Collections > [Get Collection](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/collections/get-collection)
```
GET https://{accountName}.purview.azure.com/account/collections/{collectionName}
```

## Examples
Get a collection by name.
```powershell
pv account getCollection --collectionName "g7qe97"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "collectionProvisioningState": "Succeeded",
    "friendlyName": "Environment",
    "name": "g7qe97",
    "parentCollection": {
        "referenceName": "esg-26fa7f24-pv",
        "type": "CollectionReference"
    },
    "systemData": {
        "createdAt": "2022-02-27T12:52:28.8826657Z",
        "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
        "createdByType": "User",
        "lastModifiedAt": "2022-02-27T12:52:28.8826659Z",
        "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
        "lastModifiedByType": "User"
    }
}
```
</p>
</details>