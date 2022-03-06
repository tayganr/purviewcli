# pv glossary createTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTermsAssignedEntities

## Description
Assign the given term to the provided list of related objects.

## Syntax
```
pv glossary createTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Assign Term To Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/assign-term-to-entities)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
Assign a term to one or more entities.
```powershell
pv glossary createTermsAssignedEntities --termGuid "4ba01c1e-5ef8-4457-87b4-37e2054b1cb9" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "guid": "6374e9e8-4719-4747-b2d2-054548023ae2"
    },
    {
        "guid": "dcd41879-dda2-4b3c-8c97-9b76d39799b1"
    },
    {
        "guid": "9759ea81-bb37-48ee-8099-02e452ccc57d"
    }
]
```
</p>
</details>