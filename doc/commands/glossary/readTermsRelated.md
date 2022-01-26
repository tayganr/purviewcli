# pv glossary readTermsRelated
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsRelated

## Description
Get all related terms for a specific term by its GUID. Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

## Syntax
```
pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > List Related Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-related-terms)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/related
```

## Examples
```powershell

```