# pv entity addOrUpdateBusinessMetadata
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > addOrUpdateBusinessMetadata

## Description
Add or update business metadata to an entity.

## Syntax
```
pv entity addOrUpdateBusinessMetadata --guid=<val> --payloadFile=<val> [--isOverwrite]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
`--isOverwrite` (boolean)  
Whether to overwrite the existing business metadata on the entity or not [default: false].

## API Mapping
Catalog Data Plane > Entity > [Add Or Update Business Metadata](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-or-update-business-metadata)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata
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