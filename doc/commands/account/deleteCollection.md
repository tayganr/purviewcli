# pv account deleteCollection
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > deleteCollection

## Description
Deletes a collection.

## Syntax
```
pv account deleteCollection --collectionName=<val>
```

## Required Arguments
`--collectionName` (string)  
This is the unique name of the collection (not the friendly name).

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Collections > [Delete Collection](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/collections/delete-collection)
```
DELETE https://{accountName}.purview.azure.com/account/collections/{collectionName}
```

## Examples
Delete a collection by name.
```powershell
pv account deleteCollection --collectionName "tn56xt" 
```