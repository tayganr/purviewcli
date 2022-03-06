# pv types deleteTypeDefs
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > deleteTypeDefs

## Description
Delete API for all types in bulk.

## Syntax
```
pv types deleteTypeDefs --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Delete Type Definitions](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/delete-type-definitions)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

## Examples
Delete type definitions in bulk.
```powershell
pv types deleteTypeDefs --payloadFile "/path/to/file.json"
```

<details><summary>Example payload.</summary>
<p>

```json
{
    "classificationDefs": [
        {
            "category": "CLASSIFICATION",
            "name": "CUSTOM.PII.PATIENT.IDENTITY.CARD"
        },
        {
            "category": "CLASSIFICATION",
            "name": "CUSTOM.PII.PATIENT.POLICY.NUMBER"
        }
    ],
    "entityDefs": [],
    "enumDefs": [],
    "relationshipDefs": [],
    "structDefs": []
}
```
</p>
</details>