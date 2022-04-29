# pv entity deleteBusinessMetadata
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteBusinessMetadata

## Description
Remove business metadata from an entity.

## Syntax
```
pv entity deleteBusinessMetadata --guid=<val> --payloadFile=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete Business Metadata](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-business-metadata)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata
```

## Examples
Remove business metadata from an entity.
```powershell
pv entity deleteBusinessMetadata --guid "0e945784-4bc3-40bb-a541-e8d1f7c9bf50" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "myBizMetadata1": {
        "bizAttr1": "myBizMetaData1.bizAttr1"
    }
}
```
</p>
</details>