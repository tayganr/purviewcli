# pv glossary putTerm
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putTerm

## Description
Update the given glossary term by its GUID.

## Syntax
```
pv glossary putTerm --termGuid=<val> --payloadFile=<val> [--includeTermHierarchy]
```

## Required Arguments
`--termGuid` (string)  
The globally unique identifier for glossary term.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy.

## API Mapping
Catalog Data Plane > Glossary > [Update Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/update-glossary-term)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}
```

## Examples
```powershell
pv glossary putTerm --termGuid "919e8f87-d5b2-4dde-9f6e-1bbd738536a1" --payloadFile "/path/to/file.json"
```