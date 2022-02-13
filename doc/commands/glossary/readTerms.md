# pv glossary readTerms
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTerms

## Description
Get terms by glossary name.

## Syntax
```
pv glossary readTerms [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val> --extInfo --includeTermHierarchy]
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

`--extInfo` (boolean)  
extInfo [defaul: false].

`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy [default: false].

## API Mapping
Catalog Data Plane > Glossary > [List Terms By Glossary Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-terms-by-glossary-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/glossary/name/{glossaryName}/terms
```

Catalog Data Plane > Glossary > [List Glossary Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossary-terms)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/terms
```

## Examples
Get all terms (not including term hierarchy).
```powershell
pv glossary readTerms
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "createTime": 1642161716110,
        "guid": "a91e0d7c-9504-44b8-87df-45b953e2b058",
        "longDescription": "",
        "name": "",
        "qualifiedName": "Workplace Analytics@Glossary",
        "shortDescription": null,
        "status": "Draft",
        "templateName": [],
        "updateTime": 1642161716110
    },
    {
        "createTime": 1642161716110,
        "guid": "21b5e0b7-1b24-4804-ac73-089004d46e95",
        "longDescription": "An adjustment is applied so that overlapping time is not double-counted when a person has overlapping meeting hours. For example, a person with non-declined meeting requests from 2:00 to 3:00 PM and 2:30 to 3:30 PM would yield 1.5 adjusted meeting hours.",
        "name": "Adjusted meeting hours",
        "qualifiedName": "Workplace Analytics_Adjusted meeting hours@Glossary",
        "shortDescription": null,
        "status": "Draft",
        "templateName": [],
        "updateTime": 1642161716110
    },
    {
        "createTime": 1642161716110,
        "guid": "2dea0df8-959d-455d-8283-1582c770e80e",
        "longDescription": "Aggregation means compiling data from multiple individuals or sources. The more individuals or sources whose data is used, the more difficult it is to identify personal data. Aggregation is one means of achieving de-identification.",
        "name": "Aggregation",
        "qualifiedName": "Workplace Analytics_Aggregation@Glossary",
        "shortDescription": null,
        "status": "Approved",
        "templateName": [],
        "updateTime": 1642161716110
    }
]
```
</p>
</details><br />

Get all terms (including term hierarchy).
```powershell
pv glossary readTerms --includeTermHierarchy
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "createTime": 1642161716110,
        "guid": "a91e0d7c-9504-44b8-87df-45b953e2b058",
        "longDescription": "",
        "name": "Workplace Analytics",
        "nickName": "",
        "parentTerm": null,
        "qualifiedName": "Workplace Analytics@Glossary",
        "shortDescription": null,
        "status": "Draft",
        "templateName": [],
        "updateTime": 1642161716110
    },
    {
        "createTime": 1642161716110,
        "guid": "21b5e0b7-1b24-4804-ac73-089004d46e95",
        "longDescription": "An adjustment is applied so that overlapping time is not double-counted when a person has overlapping meeting hours. For example, a person with non-declined meeting requests from 2:00 to 3:00 PM and 2:30 to 3:30 PM would yield 1.5 adjusted meeting hours.",
        "name": "Workplace Analytics_Adjusted meeting hours",
        "nickName": "Adjusted meeting hours",
        "parentTerm": null,
        "qualifiedName": "Workplace Analytics_Adjusted meeting hours@Glossary",
        "shortDescription": null,
        "status": "Draft",
        "templateName": [],
        "updateTime": 1642161716110
    },
    {
        "createTime": 1642161716110,
        "guid": "2dea0df8-959d-455d-8283-1582c770e80e",
        "longDescription": "Aggregation means compiling data from multiple individuals or sources. The more individuals or sources whose data is used, the more difficult it is to identify personal data. Aggregation is one means of achieving de-identification.",
        "name": "Workplace Analytics_Aggregation",
        "nickName": "Aggregation",
        "parentTerm": null,
        "qualifiedName": "Workplace Analytics_Aggregation@Glossary",
        "shortDescription": null,
        "status": "Approved",
        "templateName": [],
        "updateTime": 1642161716110
    }
]
```
</p>
</details>