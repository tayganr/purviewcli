# pv glossary readCategoryRelated
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategoryRelated

## Description
Get all related categories (parent and children).

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
pv glossary readCategoryRelated --categoryGuid "c856ecef-21e6-4e92-8607-9493d8432e78"
```