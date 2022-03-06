# pv glossary put
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > put

## Description
Update the given glossary.

## Syntax
```
pv glossary put --glossaryGuid=<val> --payloadFile=<val>
```

## Required Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Update Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/update-glossary)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}
```

## Examples
Update an existing glossary.
```powershell
pv glossary put --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "guid": "f2307f48-5834-4709-be85-02f3aea5d149",
    "name": "Glossary",
    "qualifiedName": "Glossary",
    "longDescription": "Hello World!"
}
```
</p>
</details>