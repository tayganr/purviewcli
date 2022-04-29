# pv entity addLabels
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > addLabels

## Description
Append labels to an entity.

## Syntax
```
pv entity addLabels --guid=<val> --payloadFile=<val>
```

## Required Arguments
`guid` (string)
DESC.

`payloadFile` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add given labels to a given entity.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-label)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/labels
```

## Examples
DESCRIBE_EXAMPLE.
```powershell
EXAMPLE_COMMAND
```
<details><summary>Example payload.</summary>
<p>

```json
PASTE_JSON_HERE
```
</p>
</details>