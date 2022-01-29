# pv policystore readMetadataPolicy
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataPolicy

## Description
Gets a metadata policy

## Syntax
```
pv policystore readMetadataPolicy (--collectionName=<val> | --policyId=<val>)
```

## Required Arguments
`--collectionName` (string)  
This unique name of the collection.

`--policyId` (string)  
The unique policy id.

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Policy > [Get](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-policy/get)
```
GET https://{accountName}.purview.azure.com/policystore/metadataPolicies/{policyId}
```

Get Metadata Policy by Collection Name
```
GET https://{accountName}.purview.azure.com/policystore/collections/{collectionName}/metadataPolicy
```

## Examples
Get a metadata policy by collection name.
```powershell
pv policystore readMetadataPolicy --collectionName "pokuj2"
```

Get a metadata policy by policy id.
```powershell
pv policystore readMetadataPolicy --policyId "67c667b7-8f1c-468f-ab3b-f19fd943de95"
```