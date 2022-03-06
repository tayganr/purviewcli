# pv types createTypeDefs
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > createTypeDefs

## Description
Create all atlas type definitions in bulk, only new definitions will be created. Any changes to the existing definitions will be discarded.

## Syntax
```
pv types createTypeDefs --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Create Type Definitions](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/create-type-definitions)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

## Examples
Create type definitions in bulk.
```powershell
pv types createTypeDefs --payloadFile "/path/to/file.json"
```

<details><summary>Example payload.</summary>
<p>

```json
{
    "classificationDefs": [
        {
            "category": "CLASSIFICATION",
            "name": "CUSTOM.PII.PATIENT.IDENTITY.CARD",
            "options": {
                "displayName": "Patient Identity Card Number"
            }
        },
        {
            "category": "CLASSIFICATION",
            "name": "CUSTOM.PII.PATIENT.POLICY.NUMBER",
            "options": {
                "displayName": "Patient Policy Number"
            }
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