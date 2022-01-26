# pv glossary readTerm
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTerm

## Description
Get a specific glossary term by its GUID.

## Syntax
```
pv glossary readTerm --termGuid=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > Get Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-glossary-term)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}
```

## Examples
```powershell

```