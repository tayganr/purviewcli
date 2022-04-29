# pv entity deleteBusinessMetadata
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteBusinessMetadata

## Description
Remove business metadata from an entity.

## Syntax
```
pv entity deleteBusinessMetadata --guid=<val>
```

## Required Arguments
`guid` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Business Metadata](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-business-metadata)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata
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