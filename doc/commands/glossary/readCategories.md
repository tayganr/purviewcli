# pv glossary readCategories
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategories

## Description
Get the categories belonging to a specific glossary.

## Syntax
```
pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

## Optional Arguments
`--limit` (integer)  
The page size [default: 1000].

`--offset` (integer)  
Offset for pagination purpose [default: 0].

`--sort` (string)  
The sort order - ASC or DESC [default: ASC].

## API Mapping
Catalog Data Plane > Glossary > [List Glossary Categories](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-categories)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/categories
```

## Examples
Get the categories belonging to a specific glossary.
```powershell
pv glossary readCategories --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149" 
```