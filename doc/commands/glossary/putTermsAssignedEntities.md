# pv glossary putTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putTermsAssignedEntities

## Description
Delete the term assignment for the given list of related objects.

## Syntax
```
pv glossary putTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Remove Term Assignment From Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/remove-term-assignment-from-entities)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
Remove the term assignment from the given list of entities.
```powershell
pv glossary putTermsAssignedEntities --termGuid "919e8f87-d5b2-4dde-9f6e-1bbd738536a1" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "guid": "9759ea81-bb37-48ee-8099-02e452ccc57d",
        "relationshipGuid": "d8f1569d-00cd-431c-8f3f-dc232e5b9b23"
    },
    {
        "guid": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
        "relationshipGuid": "ca09b79b-a86b-4285-b6f1-b6a768ce7639"
    },
    {
        "guid": "6374e9e8-4719-4747-b2d2-054548023ae2",
        "relationshipGuid": "aab7c1df-2b05-493d-b065-ca50028fc950"
    }
]
```
</p>
</details>