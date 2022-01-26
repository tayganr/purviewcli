# pv glossary readCategory
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategory

## Description
Get specific glossary category by its GUID.

## Syntax
```
pv glossary readCategory --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > Get Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-glossary-category)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}
```

## Examples
```powershell

```