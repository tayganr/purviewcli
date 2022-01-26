# pv glossary readCategoryTerms
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategoryTerms

## Description
Get all terms associated with the specific category.

## Syntax
```
pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [List Category Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-category-terms)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}/terms
```

## Examples
```powershell

```