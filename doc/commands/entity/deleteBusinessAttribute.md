# pv entity deleteBusinessAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteBusinessAttribute

## Description
Delete business metadata from an entity.

## Syntax
```
pv entity deleteBusinessAttribute --guid=<val> --bmName=<val>
```

## Required Arguments
`guid` (string)
DESC.

`bmName` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Business Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-business-attributes)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata/{bmName}
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