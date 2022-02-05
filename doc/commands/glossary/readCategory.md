# pv glossary readCategory
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategory

## Description
Get specific glossary category by its GUID.

## Syntax
```
pv glossary readCategory --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
`--categoryGuid` (string)  
The globally unique identifier of the category.

## Optional Arguments
`--limit` (integer)  
The page size [default: 1000].

`--offset` (integer)  
Offset for pagination purpose [default: 0].

`--sort` (string)  
The sort order - ASC or DESC [default: ASC].

## API Mapping
Catalog Data Plane > Glossary > [Get Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-glossary-category)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}
```

## Examples
```powershell

```