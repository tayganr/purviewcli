# pv search autoComplete
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > autoComplete

## Description
Get auto complete options.

## Syntax
```
pv search autoComplete [--keywords=<val> --limit=<val> --filterFile=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all fields that support autocomplete operation. It must be at least 1 character, and no more than 100 characters.

`--limit` (integer)  
The number of autocomplete results we hope to return. The default value is 50. The value must be a number between 1 and 100.

`--filterFile` (string)  
The filter for the search.

## API Mapping
Catalog Data Plane > Discovery > [Auto Complete](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/auto-complete)
```
POST https://{accountName}.purview.azure.com/catalog/api/search/autocomplete
```

## Examples
Auto complete options with keywords.
```powershell
pv search autoComplete --keywords "a"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "value": [
        {
            "queryPlusText": "A",
            "text": "A"
        },
        {
            "queryPlusText": "a",
            "text": "a"
        },
        {
            "queryPlusText": "Annual employee survey",
            "text": "Annual employee survey"
        },
        {
            "queryPlusText": "A less attrition",
            "text": "A less attrition"
        },
        {
            "queryPlusText": "A during a",
            "text": "A during a"
        },
        {
            "queryPlusText": "Attrition the number",
            "text": "Attrition the number"
        },
        {
            "queryPlusText": "Annual Percent Attrition",
            "text": "Annual Percent Attrition"
        },
        {
            "queryPlusText": "a part of",
            "text": "a part of"
        },
        {
            "queryPlusText": "AtlasGlossaryTerm",
            "text": "AtlasGlossaryTerm"
        },
        {
            "queryPlusText": "A plus changes",
            "text": "A plus changes"
        },
        {
            "queryPlusText": "an annual employee",
            "text": "an annual employee"
        }
    ]
}
```
</p>
</details>