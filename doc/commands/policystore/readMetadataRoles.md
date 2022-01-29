# pv policystore readMetadataRoles
[Command Reference](../../../README.md#command-reference) > [policystore](./main.md) > readMetadataRoles

## Description
Lists the metadata roles.

## Syntax
```
pv policystore readMetadataRoles
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Metadata Policy Data Plane > Metadata Roles > [List](https://docs.microsoft.com/en-us/rest/api/purview/metadatapolicydataplane/metadata-roles/list)
```
GET https://{accountName}.purview.azure.com/policystore/metadataroles
```

## Examples
Get all metadata roles.
```powershell
pv policystore readMetadataRoles
```