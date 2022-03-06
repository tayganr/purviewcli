# pv entity createBulkClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createBulkClassification

## Description
Associate a classification to multiple entities in bulk.

## Syntax
```
pv entity createBulkClassification --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add Classification](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-classification)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk/classification
```

## Examples
Associate a classification to multiple entities.
```powershell
pv entity createBulkClassification --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "classification": {
        "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
    },
    "entityGuids": [
        "c6a7811a-0699-44d0-b0be-68babe560ab2",
        "6374e9e8-4719-4747-b2d2-054548023ae2",
        "dcd41879-dda2-4b3c-8c97-9b76d39799b1"
    ]
}
```
</p>
</details>