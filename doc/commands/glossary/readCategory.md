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
pv glossary readCategory --categoryGuid "c856ecef-21e6-4e92-8607-9493d8432e78"
```
<details><summary>Sample response.</summary>
<p>

```json
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
```
</p>
</details>