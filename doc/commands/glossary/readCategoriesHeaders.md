# pv glossary readCategoriesHeaders
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategoriesHeaders

## Description
Get the category headers belonging to a specific glossary.

## Syntax
```
pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [List Glossary Categories Headers](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-categories-headers)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/categories/headers
```

## Examples
```powershell

```