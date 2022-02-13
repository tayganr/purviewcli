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
```powershell
pv glossary putTermsAssignedEntities --termGuid "919e8f87-d5b2-4dde-9f6e-1bbd738536a1" --payloadFile "/path/to/file.json"
```