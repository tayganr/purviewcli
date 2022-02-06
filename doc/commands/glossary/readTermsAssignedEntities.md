# pv glossary readTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsAssignedEntities

## Description
Get all related objects assigned with the specified term.

## Syntax
```
pv glossary readTermsAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
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
Catalog Data Plane > Glossary > [Get Entities Assigned With Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-entities-assigned-with-term)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
Get all entities associated to a glossary term.
```powershell
pv glossary readTermsAssignedEntities --termGuid "0d8c0610-4c8b-4f90-b18b-e85d688eb2e6"
```

<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "displayText": "Customer",
        "entityStatus": "ACTIVE",
        "guid": "92b8816a-d0f7-42e6-b840-c4f6f6f60000",
        "relationshipAttributes": {
            "attributes": {
                "confidence": null,
                "createdBy": null,
                "description": null,
                "expression": null,
                "source": null,
                "status": null,
                "steward": null
            },
            "typeName": "AtlasGlossarySemanticAssignment"
        },
        "relationshipGuid": "9127c28a-6db4-4260-b6b3-c5de02b954f8",
        "relationshipStatus": "ACTIVE",
        "relationshipType": "AtlasGlossarySemanticAssignment",
        "typeName": "azure_sql_table"
    },
    {
        "displayText": "Address",
        "entityStatus": "ACTIVE",
        "guid": "c59b3388-e71b-4a1b-9840-a1f6f6f60000",
        "relationshipAttributes": {
            "attributes": {
                "confidence": null,
                "createdBy": null,
                "description": null,
                "expression": null,
                "source": null,
                "status": null,
                "steward": null
            },
            "typeName": "AtlasGlossarySemanticAssignment"
        },
        "relationshipGuid": "acd4f1af-29f6-450a-b7df-868eea37065d",
        "relationshipStatus": "ACTIVE",
        "relationshipType": "AtlasGlossarySemanticAssignment",
        "typeName": "azure_sql_table"
    }
]
```
</p>
</details>