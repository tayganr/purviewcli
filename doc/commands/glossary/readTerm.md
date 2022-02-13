# pv glossary readTerm
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTerm

## Description
Get a specific glossary term by its GUID.

## Syntax
```
pv glossary readTerm --termGuid=<val> [--includeTermHierarchy]
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy [default: false].

## API Mapping
Catalog Data Plane > Glossary > [Get Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-glossary-term)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}
```

## Examples
Get a glossary term.
```powershell
pv glossary readTerm --termGuid "21b5e0b7-1b24-4804-ac73-089004d46e95"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "abbreviation": "AMH",
    "anchor": {
        "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
        "relationGuid": "5a1caddc-5401-4b9f-96b1-6f87b9e8583e"
    },
    "createTime": 1642161716110,
    "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
    "guid": "21b5e0b7-1b24-4804-ac73-089004d46e95",
    "lastModifiedTS": "1",
    "longDescription": "An adjustment is applied so that overlapping time is not double-counted when a person has overlapping meeting hours. For example, a person with non-declined meeting requests from 2:00 to 3:00 PM and 2:30 to 3:30 PM would yield 1.5 adjusted meeting hours.",
    "name": "Workplace Analytics_Adjusted meeting hours",
    "qualifiedName": "Workplace Analytics_Adjusted meeting hours@Glossary",
    "resources": [
        {
            "displayName": "Workspace Analytics",
            "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
        }
    ],
    "status": "Draft",
    "updateTime": 1642161716110,
    "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
}
```
</p>
</details>