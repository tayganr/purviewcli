# pv glossary readTermsRelated
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsRelated

## Description
Get all related terms for a specific term by its GUID. Limit, offset, and sort parameters are currently not being enabled and won't work even they are passed.

## Syntax
```
pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

## Optional Arguments
`--limit` (integer)  
The page size [default: 1000].

`--offset` (integer)  
Offset for pagination purpose [default: 0].

`--sort` (string)  
The sort order - ASC or DESC [default: ASC].

## API Mapping
Catalog Data Plane > Glossary > [List Related Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-related-terms)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/related
```

## Examples
Get all related terms for a specific term (e.g. Synonyms and Related Terms).
```powershell
pv glossary readTermsRelated --termGuid "c059801e-5202-4b2c-8c41-6fc82f8404a0"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "seeAlso": [
        {
            "displayText": "Workplace Analytics_Meeting",
            "relationGuid": "47e3b5e4-cfc3-4780-bab9-91041b68acf5",
            "termGuid": "0d8c0610-4c8b-4f90-b18b-e85d688eb2e6"
        },
        {
            "displayText": "Workplace Analytics_Attendee",
            "relationGuid": "efe0da8f-d612-4c75-b821-a6abc20bf35d",
            "termGuid": "09a7f806-8612-4de4-b87a-5481f6e2878c"
        }
    ],
    "synonyms": [
        {
            "displayText": "Workplace Analytics_Attendee",
            "relationGuid": "df33c998-9623-44e7-90a0-d595aff476c3",
            "termGuid": "09a7f806-8612-4de4-b87a-5481f6e2878c"
        }
    ]
}
```
</p>
</details>