# pv entity addLabels
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > addLabels

## Description
Append labels to an entity.

## Syntax
```
pv entity addLabels --guid=<val> --payloadFile=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add given labels to a given entity.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-label)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/labels
```

## Examples
Append labels to an existing entity.
```powershell
pv entity addLabels --guid "7738b5c7-7977-4261-9871-7d00e11cabe8" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    "a",
    "b",
    "c"
]
```
</p>
</details>