# pv glossary deleteCategory
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > deleteCategory

## Description
Delete a glossary category.

## Syntax
```
pv glossary deleteCategory --categoryGuid=<val>
```

## Required Arguments
`--categoryGuid` (string)  
The globally unique identifier of the category.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Delete Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/delete-glossary-category)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}
```

## Examples
Delete a category.
```powershell
pv glossary deleteCategory --categoryGuid "bba73040-db31-4025-8e03-a8eb27fc0822"
```