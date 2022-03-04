# pv search suggest
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > suggest

## Description
Get search suggestions by query criteria.

## Syntax
```
pv search suggest [--keywords=<val> --limit=<val> --filterFile=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all fields that support suggest operation. It must be at least 1 character, and no more than 100 characters.

`--limit` (integer)  
The number of suggestions we hope to return. The default value is 5. The value must be a number between 1 and 100.

`--filterFile` (string)  
The filter for the search.

## API Mapping
Catalog Data Plane > Discovery > [Suggest](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/suggest)
```
POST https://{accountName}.purview.azure.com/catalog/api/search/suggest
```

## Examples
Search suggestions by keywords.
```powershell
pv search suggest --keywords "Sta"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "value": [
        {
            "@search.score": 5.925384,
            "@search.text": "Growth <em>Stage</em> of Company",
            "assetType": null,
            "classification": [],
            "collectionId": null,
            "description": null,
            "entityType": "AtlasGlossaryTerm",
            "id": "39cd231f-9571-4dee-afff-5c2841938945",
            "label": [],
            "name": "Growth Stage of Company",
            "owner": null,
            "qualifiedName": "General_Growth Stage of Company@Glossary",
            "term": []
        }
    ]
}
```
</p>
</details>