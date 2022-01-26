# pv glossary readCategories
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategories

## Description
Get the categories belonging to a specific glossary.

## Syntax
```
pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > List Glossary Categories](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-categories)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/categories
```

## Examples
```powershell

```