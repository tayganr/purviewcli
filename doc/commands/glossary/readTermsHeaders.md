# pv glossary readTermsHeaders
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsHeaders

## Description
Get term headers belonging to a specific glossary.

## Syntax
```
pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [List Glossary Term Headers](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-term-headers)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/terms/headers
```

## Examples
```powershell

```