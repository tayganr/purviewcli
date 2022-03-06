# pv glossary createCategories
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createCategories

## Description
Create glossary category in bulk.

## Syntax
```
pv glossary createCategories --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Create Glossary Categories](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/create-glossary-categories)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/categories
```

## Examples
Create categories in bulk.
```powershell
pv glossary createCategories --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "anchor": {
            "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149"
        },
        "name": "Category1"
    },
    {
        "anchor": {
            "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149"
        },
        "name": "Category2"
    }
]
```
</p>
</details>