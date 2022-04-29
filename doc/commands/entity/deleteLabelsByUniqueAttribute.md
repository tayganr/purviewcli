# pv entity deleteLabelsByUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteLabelsByUniqueAttribute

## Description
Delete label(s) from an entity identified by its type and unique attributes.

## Syntax
```
pv entity deleteLabelsByUniqueAttribute --typeName=<val> --qualifiedName=<val>
```

## Required Arguments
`typeName` (string)
DESC.

`qualifiedName` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete given labels to a given entity identified by its type and unique attributes.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-labels-by-unique-attribute)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/labels
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