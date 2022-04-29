# pv entity addLabelsByUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > addLabelsByUniqueAttribute

## Description
Append labels to an entity identified by its type and unique attributes.

## Syntax
```
pv entity addLabelsByUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
```

## Required Arguments
`typeName` (string)
DESC.

`qualifiedName` (string)
DESC.

`payloadFile` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add given labels to a given entity identified by its type and unique attributes.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-labels-by-unique-attribute)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/labels
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