# pv account getCollectionPath
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getCollectionPath

## Description
Gets the parent name and parent friendly name chains that represent the collection path.

## Syntax
```
pv account getCollectionPath --collectionName=<val>
```

## Required Arguments
`--collectionName` (string)  
This is the unique name of the collection (not the friendly name).

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Collections > [Get Collection Path](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/collections/get-collection-path)
```
GET https://{accountName}.purview.azure.com/account/collections/{collectionName}/getCollectionPath
```

## Examples
```powershell

```