# pv glossary readCategoriesHeaders
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategoriesHeaders

## Description
Get the category headers belonging to a specific glossary.

## Syntax
```
pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
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
Catalog Data Plane > Glossary > [List Glossary Categories Headers](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-categories-headers)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/categories/headers
```

## Examples
```powershell
pv glossary readCategoriesHeaders --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149"
```
<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "categoryGuid": "5a5a79b4-52eb-4540-ba1a-001458e5d257",
        "displayText": "Category1",
        "relationGuid": "20f62759-22e8-4acf-8757-1da8f12d8eb3"
    },
    {
        "categoryGuid": "c856ecef-21e6-4e92-8607-9493d8432e78",
        "displayText": "MyCategory",
        "relationGuid": "02a36a2f-e240-40ea-b884-c5ec159d5688"
    }
]
```
</p>
</details><br />