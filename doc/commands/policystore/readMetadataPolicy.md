# pv policystore readMetadataPolicy
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataPolicy

## Description
Gets a metadata policy

## Syntax
```
pv policystore readMetadataPolicy (--collectionName=<val> | --policyId=<val>)
```

## Required Arguments
*None*

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
```powershell

```