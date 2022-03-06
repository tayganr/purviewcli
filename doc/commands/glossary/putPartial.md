# pv glossary putPartial
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putPartial

## Description
Update the glossary partially.

## Syntax
```
pv glossary putPartial --glossaryGuid=<val> --payloadFile=<val> [--includeTermHierarchy]
```

## Required Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy [default: false].

## API Mapping
Catalog Data Plane > Glossary > [Partial Update Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/partial-update-glossary)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/partial
```

## Examples
Update an existing glossary.
```powershell
pv glossary putPartial --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "longDescription": "This is a long description!"
}
```
</p>
</details>