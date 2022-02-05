# pv glossary readCategoryRelated
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategoryRelated

## Description
Get all related categories (parent and children). Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

## Syntax
```
pv glossary readCategoryRelated --categoryGuid=<val>
```

## Required Arguments
`--categoryGuid` (string)  
The globally unique identifier of the category.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [List Related Categories](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-related-categories)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}/related
```

## Examples
```powershell

```