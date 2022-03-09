# pv glossary createTerms
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTerms

## Description
Create glossary terms in bulk.

## Syntax
```
pv glossary createTerms --payloadFile=<val> [--includeTermHierarchy]
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy [default: false].

## API Mapping
Catalog Data Plane > Glossary > [Create Glossary Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/create-glossary-terms)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms
```

## Examples
Create terms in bulk.
```powershell
pv glossary createTerms --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "anchor": {
            "glossaryGuid": "125e2575-5823-4887-89f0-ff03a70f7c3a"
        },
        "longDescription": "This is a definition for Term1.",
        "name": "Term1"
    },
    {
        "anchor": {
            "glossaryGuid": "125e2575-5823-4887-89f0-ff03a70f7c3a"
        },
        "longDescription": "This is a definition for Term2.",
        "name": "Term2"
    },
    {
        "anchor": {
            "glossaryGuid": "125e2575-5823-4887-89f0-ff03a70f7c3a"
        },
        "longDescription": "This is a definition for Term3.",
        "name": "Term3"
    }    
]
```
</p>
</details><br/>

Create terms in bulk with a custom term template. Note: The payload has the additional "attributes" property.
```powershell
pv glossary createTerms --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "anchor": {
            "glossaryGuid": "9a799256-4992-4571-9c39-1d7e3ff61470"
        },
        "attributes": {
            "My Custom Term Template": {
                "Custom Attribute 01": "Hello World",
                "Custom Attribute 02": "Hello World"
            }
        },
        "longDescription": "This is a definition for Term1.",
        "name": "Term1"
    },
    {
        "anchor": {
            "glossaryGuid": "9a799256-4992-4571-9c39-1d7e3ff61470"
        },
        "attributes": {
            "My Custom Term Template": {
                "Custom Attribute 01": "Hello World",
                "Custom Attribute 02": "Hello World"
            }
        },
        "longDescription": "This is a definition for Term2.",
        "name": "Term2"
    },
    {
        "anchor": {
            "glossaryGuid": "9a799256-4992-4571-9c39-1d7e3ff61470"
        },
        "attributes": {
            "My Custom Term Template": {
                "Custom Attribute 01": "Hello World",
                "Custom Attribute 02": "Hello World"
            }
        },
        "longDescription": "This is a definition for Term3.",
        "name": "Term3"
    }    
]
```
</p>
</details>