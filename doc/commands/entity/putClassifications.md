# pv entity putClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > putClassifications

## Description
Update classifications to an existing entity represented by a guid.

## Syntax
```
pv entity putClassifications --guid=<val> --payloadFile=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Update Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/update-classifications)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classifications
```

## Examples
Update existing classifications to an existing entity via the entity GUID.
```powershell
pv entity putClassifications --guid "bbb9ff1d-f880-435e-ac87-d6fd5676d8f0" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[

    {
        "typeName": "MICROSOFT.FINANCIAL.CREDIT_CARD_NUMBER",
        "attributes": {
            "confidence": 2
        }
    }
]
```
</p>
</details>