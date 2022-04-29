# pv types readBusinessMetadataDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readBusinessMetadataDef

## Description
Get the business metadata definition by GUID or its name (unique).

## Syntax
```
pv types readBusinessMetadataDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`guid` (string)
DESC.

`name` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get the businessMetadata definition by it's name (unique).](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-business-metadata-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/businessmetadatadef/name/{name}
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