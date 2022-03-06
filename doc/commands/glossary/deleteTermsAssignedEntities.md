# pv glossary deleteTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > deleteTermsAssignedEntities

## Description
Delete the term assignment for the given list of related objects.

## Syntax
```
pv glossary deleteTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Delete Term Assignment From Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/delete-term-assignment-from-entities)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
Remove term assignments in bulk.
```powershell
pv glossary deleteTermsAssignedEntities --termGuid "bcf9fa54-9c28-4e8d-8775-ccb60785aab9" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "guid": "9759ea81-bb37-48ee-8099-02e452ccc57d",
        "relationshipGuid": "cecdb42a-bfa5-4576-a883-ccf40b219672"
    },
    {
        "guid": "6374e9e8-4719-4747-b2d2-054548023ae2",
        "relationshipGuid": "784ab0f6-e2eb-4dd6-a4b8-83d78b6504b7"
    },
    {
        "guid": "dcd41879-dda2-4b3c-8c97-9b76d39799b1",
        "relationshipGuid": "ff69eb83-dec3-491b-b7ec-4dcb303652a1"
    }
]
```
</p>
</details>