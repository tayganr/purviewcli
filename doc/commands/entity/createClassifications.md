# pv entity createClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createClassifications

## Description
Add classifications to an existing entity represented by a GUID.

## Syntax
```
pv entity createClassifications --guid=<val> --payloadFile=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-classifications)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classifications
```

## Examples
Associate an entity to multiple classifications.
```powershell
pv entity createClassifications --guid "04f2bb30-91db-404b-a8e1-d65e45338929" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
    },
    {
        "typeName": "MICROSOFT.FINANCIAL.CREDIT_CARD_NUMBER"
    }
]
```
</p>
</details>