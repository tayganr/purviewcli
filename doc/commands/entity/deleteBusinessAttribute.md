# pv entity deleteBusinessAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteBusinessAttribute

## Description
Delete business metadata from an entity.

## Syntax
```
pv entity deleteBusinessAttribute --guid=<val> --bmName=<val> --payloadFile=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--bmName` (string)  
The name of the business metadata.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Business Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-business-attributes)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata/{bmName}
```

## Examples
Delete business metadata from an entity.
```powershell
pv entity deleteBusinessAttribute --guid "0e945784-4bc3-40bb-a541-e8d1f7c9bf50" --bmName "myBizMetadata1" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "bizAttr1": "bizAttr1"
}
```
</p>
</details>