# pv glossary putCategoryPartial
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putCategoryPartial

## Description
Update the glossary category partially.

## Syntax
```
pv glossary putCategoryPartial --categoryGuid=<val> --payloadFile=<val>
```

## Required Arguments
`--categoryGuid` (string)  
The globally unique identifier of the category.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Partial Update Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/partial-update-glossary-category)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}/partial
```

## Examples
Updated simple attributes of a category.
```powershell
pv glossary putCategoryPartial --categoryGuid "c856ecef-21e6-4e92-8607-9493d8432e78" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "longDescription": "Example Long Description"
}
```
</p>
</details>