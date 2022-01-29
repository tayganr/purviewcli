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
pv account putCollection --friendlyName "newColl" --parentCollection "pvlab-taygan2-pv"
```