# pv policystore readMetadataPolicies
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataPolicies

## Description
List all metadata policies.

## Syntax
```
pv policystore readMetadataPolicies
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Policy > [List All](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-policy/list-all)
```
GET https://{accountName}.purview.azure.com/policystore/metadataPolicies
```

## Examples
Get all metadata policies.
```powershell
pv policystore readMetadataPolicies
```