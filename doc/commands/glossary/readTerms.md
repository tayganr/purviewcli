# pv glossary readTerms
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTerms

## Description
Get terms by glossary name.

## Syntax
```
pv glossary readTerms [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val> --extInfo --includeTermHierarchy]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [List Terms By Glossary Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-terms-by-glossary-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/glossary/name/{glossaryName}/terms
```

Catalog Data Plane > Glossary > [List Glossary Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-terms)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/terms
```

## Examples
```powershell

```