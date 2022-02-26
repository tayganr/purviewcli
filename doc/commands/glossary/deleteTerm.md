# pv glossary deleteTerm
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > deleteTerm

## Description
Delete a glossary term.

## Syntax
```
pv glossary deleteTerm --termGuid=<val>
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Delete Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/delete-glossary-term)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}
```

## Examples
Delete a term.
```powershell
pv glossary deleteTerm --termGuid "fb035cf8-aeb2-44b1-9fdf-d532dd26a5f0"
```