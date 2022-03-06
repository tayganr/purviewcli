# pv glossary putTermPartial
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putTermPartial

## Description
Update the glossary term partially.

## Syntax
```
pv glossary putTermPartial --termGuid=<val> --payloadFile=<val> [--includeTermHierarchy]
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
Catalog Data Plane > Glossary > [Partial Update Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/partial-update-glossary-term)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}/partial
```

## Examples
Update a basic attribute of an existing glossary term.
```powershell
pv glossary putTermPartial --termGuid "919e8f87-d5b2-4dde-9f6e-1bbd738536a1" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "longDescription": "Updated description!"
}
```
</p>
</details>