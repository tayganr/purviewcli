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
pv account getCollection --collectionName "fkcbkx"
```