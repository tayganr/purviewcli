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
Get all categories belonging to a specific glossary.
```powershell
pv glossary readCategories --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149" 
```
<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "anchor": {
            "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
            "relationGuid": "20f62759-22e8-4acf-8757-1da8f12d8eb3"
        },
        "guid": "5a5a79b4-52eb-4540-ba1a-001458e5d257",
        "lastModifiedTS": "1",
        "name": "Category1",
        "qualifiedName": "Category1@Glossary"
    },
    {
        "anchor": {
            "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
            "relationGuid": "02a36a2f-e240-40ea-b884-c5ec159d5688"
        },
        "guid": "c856ecef-21e6-4e92-8607-9493d8432e78",
        "lastModifiedTS": "1",
        "name": "MyCategory",
        "qualifiedName": "MyCategory@Glossary"
    }
]
```
</p>
</details><br />