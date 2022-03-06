# pv glossary create
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > create

## Description
Create a glossary.

## Syntax
```
pv glossary create --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Create Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/create-glossary)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary
```

## Examples
Create a glossary.
```powershell
pv glossary create --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "name": "MyGlossary",
    "qualifiedName": "MyGlossary"
}
```
</p>
</details>