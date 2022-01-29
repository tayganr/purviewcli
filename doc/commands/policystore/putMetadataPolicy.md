# pv policystore putMetadataPolicy
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > putMetadataPolicy

## Description
Updates a metadata policy

## Syntax
```
pv policystore putMetadataPolicy --policyId=<val> --payload-file=<val>
```

## Required Arguments
`--policyId` (string)  
The unique policy id.

`--payload-file` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Policy > [Update](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-policy/update)
```
PUT https://{accountName}.purview.azure.com/policystore/metadataPolicies/{policyId}
```

## Examples
```powershell
 pv policystore putMetadataPolicy --policyId "67c667b7-8f1c-468f-ab3b-f19fd943de95" --payload-file "/Path/to/file.json"
```