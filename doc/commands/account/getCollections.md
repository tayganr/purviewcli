# pv account getCollections
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getCollections

## Description
List the collections in the account.

## Syntax
```
pv account getCollections
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Collections > [List Collections](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/collections/list-collections)
```
GET https://{accountName}.purview.azure.com/account/collections
```

## Examples
List collections in the account.
```powershell
pv account getCollections
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 4,
    "value": [
        {
            "collectionProvisioningState": "Succeeded",
            "description": "The root collection.",
            "friendlyName": "My Friendly Collection Name",
            "name": "esg-26fa7f24-pv",
            "systemData": {
                "createdAt": "2022-02-23T09:46:46.2381767Z",
                "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "createdByType": "User",
                "lastModifiedAt": "2022-02-23T15:45:37.0561952Z",
                "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "lastModifiedByType": "User"
            }
        },
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
        },
        {
            "collectionProvisioningState": "Succeeded",
            "friendlyName": "Social",
            "name": "6b93rz",
            "parentCollection": {
                "referenceName": "esg-26fa7f24-pv",
                "type": "CollectionReference"
            },
            "systemData": {
                "createdAt": "2022-02-27T12:52:36.1509462Z",
                "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "createdByType": "User",
                "lastModifiedAt": "2022-02-27T12:52:36.1509463Z",
                "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "lastModifiedByType": "User"
            }
        },
        {
            "collectionProvisioningState": "Succeeded",
            "friendlyName": "Governance",
            "name": "bfgnyg",
            "parentCollection": {
                "referenceName": "esg-26fa7f24-pv",
                "type": "CollectionReference"
            },
            "systemData": {
                "createdAt": "2022-02-27T12:52:43.3993723Z",
                "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "createdByType": "User",
                "lastModifiedAt": "2022-02-27T12:52:43.3993724Z",
                "lastModifiedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "lastModifiedByType": "User"
            }
        }
    ]
}
```
</p>
</details>