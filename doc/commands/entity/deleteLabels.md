# pv entity deleteLabels
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteLabels

## Description
Delete Labels

## Syntax
```
pv entity deleteLabels --guid=<val>
```

## Required Arguments
`guid` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete given labels to a given entity.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-labels)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/labels
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