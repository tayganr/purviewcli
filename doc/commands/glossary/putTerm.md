# pv glossary putTerm
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putTerm

## Description
Update the given glossary term by its GUID.

## Syntax
```
pv glossary putTerm --termGuid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Update Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/update-glossary-term)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}
```

## Examples
```powershell

```