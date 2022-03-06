# pv types putTypeDefs
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > putTypeDefs

## Description
Update all types in bulk, changes detected in the type definitions would be persisted.

## Syntax
```
pv types putTypeDefs --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Update Atlas Type Definitions](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/update-atlas-type-definitions)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

## Examples
Update type definitions in bulk.
```powershell
pv types putTypeDefs --payloadFile "/path/to/file.json"
```

<details><summary>Example payload.</summary>
<p>

```json
{
    "classificationDefs": [
        {
            "category": "CLASSIFICATION",
            "name": "CUSTOM.PII.PATIENT.IDENTITY.CARD",
            "description": "Positively identifying patients ensures intended patient receives the intended care.",
            "options": {
                "displayName": "Patient Identity Card Number"
            }
        },
        {
            "category": "CLASSIFICATION",
            "name": "CUSTOM.PII.PATIENT.POLICY.NUMBER",
            "description": "The number of the insurance policy as assigned by the Insurer.",
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