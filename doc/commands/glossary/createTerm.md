# pv glossary createTerm
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTerm

## Description
Create a glossary term.

## Syntax
```
pv glossary createTerm --payloadFile=<val> [--includeTermHierarchy]
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy [default: false].

## API Mapping
Catalog Data Plane > Glossary > [Create Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/create-glossary-term)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term
```

## Examples
Create a term.
```powershell
pv glossary createTerm --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "anchor": {
        "glossaryGuid": "125e2575-5823-4887-89f0-ff03a70f7c3a"
    },
    "longDescription": "This is a basic term definition with no parent.",
    "name": "My Basic Term"
}
```
</p>
</details>