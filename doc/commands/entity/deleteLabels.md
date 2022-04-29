# pv entity deleteLabels
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteLabels

## Description
Delete label(s) from an entity.

## Syntax
```
pv entity deleteLabels --guid=<val> --payloadFile=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete given labels to a given entity.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-labels)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/labels
```

## Examples
Delete labels from an existing entity.
```powershell
pv entity deleteLabels --guid "7738b5c7-7977-4261-9871-7d00e11cabe8" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    "a",
    "c"
]
```
</p>
</details>