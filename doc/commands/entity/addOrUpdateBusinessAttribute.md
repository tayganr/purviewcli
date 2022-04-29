# pv entity addOrUpdateBusinessAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > addOrUpdateBusinessAttribute

## Description
Add or update business attributes to an entity.

## Syntax
```
pv entity addOrUpdateBusinessAttribute --guid=<val> --payloadFile=<val> --bmName=<val>
```

## Required Arguments
`guid` (string)
DESC.

`payloadFile` (string)
DESC.

`bmName` (string)
DESC.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add Or Update Business Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-or-update-business-attributes)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata/{bmName}
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