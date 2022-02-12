# pv glossary read
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > read

## Description
Get all glossaries registered with Atlas.

## Syntax
```
pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val> --ignoreTermsAndCategories]
```

## Required Arguments
*None*

## Optional Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

`--limit` (integer)  
The page size [default: 1000].

`--offset` (integer)  
Offset for pagination purpose [default: 0].

`--sort` (string)  
The sort order - ASC or DESC [default: ASC].

`--ignoreTermsAndCategories` (boolean)  
Whether to ignore terms and categories [default: false].

## API Mapping
Catalog Data Plane > Glossary > [List Glossaries](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossaries)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary
```

Catalog Data Plane > Glossary > [Get Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-glossary)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}
```

## Examples
Get all glossaries (without terms and categories).
```powershell
pv glossary read --ignoreTermsAndCategories
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "guid": "f2307f48-5834-4709-be85-02f3aea5d149",
        "lastModifiedTS": "1",
        "name": "Glossary",
        "qualifiedName": "Glossary"
    }
]
```
</p>
</details><br />

Get all glossaries.
```powershell
pv glossary read
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "guid": "f2307f48-5834-4709-be85-02f3aea5d149",
        "lastModifiedTS": "1",
        "name": "Glossary",
        "qualifiedName": "Glossary",
        "terms": [
            {
                "displayText": "Workplace Analytics_Insularity",
                "relationGuid": "77849f80-ceba-4ca0-bf89-f7410833adeb",
                "termGuid": "982f2110-f53d-4c62-96aa-ab8f1754f1b8"
            },
            {
                "displayText": "Workplace Analytics_Collaborator group",
                "relationGuid": "b13bd0f2-5729-4999-a31c-08c71c59312e",
                "termGuid": "7770ef0f-74e0-43a1-bb6a-8eab9d5dce13"
            },
            {
                "displayText": "Workplace Analytics_Adjusted meeting hours",
                "relationGuid": "5a1caddc-5401-4b9f-96b1-6f87b9e8583e",
                "termGuid": "21b5e0b7-1b24-4804-ac73-089004d46e95"
            }
        ]
    }
]
```
</p>
</details><br />

Get a specific glossary.
```powershell
pv glossary read --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "guid": "f2307f48-5834-4709-be85-02f3aea5d149",
    "lastModifiedTS": "1",
    "name": "Glossary",
    "qualifiedName": "Glossary",
    "terms": [
        {
            "displayText": "Workplace Analytics_Insularity",
            "relationGuid": "77849f80-ceba-4ca0-bf89-f7410833adeb",
            "termGuid": "982f2110-f53d-4c62-96aa-ab8f1754f1b8"
        },
        {
            "displayText": "Workplace Analytics_Collaborator group",
            "relationGuid": "b13bd0f2-5729-4999-a31c-08c71c59312e",
            "termGuid": "7770ef0f-74e0-43a1-bb6a-8eab9d5dce13"
        },
        {
            "displayText": "Workplace Analytics_Adjusted meeting hours",
            "relationGuid": "5a1caddc-5401-4b9f-96b1-6f87b9e8583e",
            "termGuid": "21b5e0b7-1b24-4804-ac73-089004d46e95"
        }
    ]
}
```
</p>
</details>