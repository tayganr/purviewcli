# pv glossary createCategory
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createCategory

## Description
Create a glossary category.

## Syntax
```
pv glossary createCategory --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Create Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/create-glossary-category)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category
```

## Examples
Create a new category.
```powershell
pv glossary createCategory --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "anchor": {
        "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149"
    },
    "name": "MyCategory"
}
```
</p>
</details>