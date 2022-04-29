# pv entity addOrUpdateBusinessAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > addOrUpdateBusinessAttribute

## Description
Add or update business attributes to an entity.

## Syntax
```
pv entity addOrUpdateBusinessAttribute --guid=<val> --bmName=<val> --payloadFile=<val>
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
Catalog Data Plane > Entity > [Add Or Update Business Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-or-update-business-attributes)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/businessmetadata/{bmName}
```

## Examples
Add or update business attributes to an entity.
```powershell
pv entity addOrUpdateBusinessAttribute --guid "0e945784-4bc3-40bb-a541-e8d1f7c9bf50" --bmName "myBizMetadata1" --payloadFile "/path/to/file.json"
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