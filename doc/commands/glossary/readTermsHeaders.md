# pv glossary readTermsHeaders
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsHeaders

## Description
Get term headers belonging to a specific glossary.

## Syntax
```
pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
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
Catalog Data Plane > Glossary > [List Glossary Term Headers](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-term-headers)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/terms/headers
```

## Examples
Get glossary term headers.
```powershell
pv glossary readTermsHeaders --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149"
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "displayText": "Workplace Analytics",
        "relationGuid": "8de510cd-7455-4b8d-9356-c5e39eb1c3be",
        "termGuid": "a91e0d7c-9504-44b8-87df-45b953e2b058"
    },
    {
        "displayText": "Workplace Analytics_Adjusted meeting hours",
        "relationGuid": "5a1caddc-5401-4b9f-96b1-6f87b9e8583e",
        "termGuid": "21b5e0b7-1b24-4804-ac73-089004d46e95"
    },
    {
        "displayText": "Workplace Analytics_Aggregation",
        "relationGuid": "a7a378ef-a2a5-4b56-bd19-4f84f4b32446",
        "termGuid": "2dea0df8-959d-455d-8283-1582c770e80e"
    },
    {
        "displayText": "Workplace Analytics_Attended",
        "relationGuid": "6f95e12c-7dc2-4320-beb6-497d34f4a34d",
        "termGuid": "c059801e-5202-4b2c-8c41-6fc82f8404a0"
    }
]
```
</p>
</details>