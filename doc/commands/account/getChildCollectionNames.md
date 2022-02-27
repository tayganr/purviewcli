# pv account getChildCollectionNames
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getChildCollectionNames

## Description
Lists the child collections names in the collection.

## Syntax
```
pv account getChildCollectionNames --collectionName=<val>
```

## Required Arguments
`--collectionName` (string)  
This is the unique name of the collection (not the friendly name).

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Collections > [List Child Collection Names](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/collections/list-child-collection-names)
```
GET https://{accountName}.purview.azure.com/account/collections/{collectionName}/getChildCollectionNames
```

## Examples
List the child collections beneath a target collection.
```powershell
pv account getChildCollectionNames --collectionName "esg-26fa7f24-pv"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 3,
    "value": [
        {
            "friendlyName": "Environment",
            "name": "g7qe97"
        },
        {
            "friendlyName": "Social",
            "name": "6b93rz"
        },
        {
            "friendlyName": "Governance",
            "name": "bfgnyg"
        }
    ]
}
```
</p>
</details>