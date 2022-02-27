# pv glossary delete
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > delete

## Description
Delete a glossary.

## Syntax
```
pv glossary delete --glossaryGuid=<val>
```

## Required Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Delete Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/delete-glossary)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}
```

## Examples
Delete a glossary.
```powershell
pv glossary delete --glossaryGuid "ac6ddb6d-d53f-4df7-b6d8-a4c29aca1447"
```