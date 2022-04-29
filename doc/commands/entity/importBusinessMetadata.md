# pv entity importBusinessMetadata
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > importBusinessMetadata

## Description
 Import business metadata in bulk.

## Syntax
```
pv entity importBusinessMetadata --bmFile=<val>
```

## Required Arguments
`bmFile` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Import Business Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/import-business-attributes)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/businessmetadata/import
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