# pv glossary putCategory
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putCategory

## Description
Update the given glossary category by its GUID.

## Syntax
```
pv glossary putCategory --categoryGuid=<val> --payloadFile=<val>
```

## Required Arguments
`--categoryGuid` (string)  
The globally unique identifier of the category.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Update Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/update-glossary-category)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}
```

## Examples
Update an existing category.
```powershell
pv glossary putCategory --categoryGuid "c856ecef-21e6-4e92-8607-9493d8432e78" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "anchor": {
        "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149"
    },
    "guid": "c856ecef-21e6-4e92-8607-9493d8432e78",
    "name": "MyCategory",
    "terms": [
        {
            "termGuid": "d99523b1-9b89-4748-8455-c00d76fd823a"
        },
        {
            "termGuid": "06276c6f-aab7-46f3-980c-e92ad541f333"
        },
        {
            "termGuid": "2796d276-75a0-46c0-9920-1d9e75c25842"
        }
    ]
}
```
</p>
</details>