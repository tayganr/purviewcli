# pv entity put
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > put

## Description
Update entity partially by its GUID. Supports only primitive attribute type and entity references. It does not support updating complex types like arrays, and maps. Null updates are not possible.

## Syntax
```
pv entity put --guid=<val> --attrName=<val> --attrValue=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--attrName` (string)  
The name of the attribute.

`--attrValue` (string)  
The value of the attribute.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Partial Update Entity Attribute By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/partial-update-entity-attribute-by-guid)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}
```

## Examples
Perform a partial update on an existing entity.
```powershell
pv entity put --guid "a20331b9-c1b3-48c3-8072-59f06ba1ba39" --attrName "description" --attrValue "hello world"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "guidAssignments": {},
    "mutatedEntities": {
        "PARTIAL_UPDATE": [
            {
                "attributes": {
                    "qualifiedName": null
                },
                "guid": "a20331b9-c1b3-48c3-8072-59f06ba1ba39",
                "lastModifiedTS": "2",
                "typeName": "azure_datalake_gen2_path"
            }
        ]
    },
    "partialUpdatedEntities": [
        {
            "attributes": {
                "qualifiedName": null
            },
            "guid": "a20331b9-c1b3-48c3-8072-59f06ba1ba39",
            "lastModifiedTS": "2",
            "typeName": "azure_datalake_gen2_path"
        }
    ]
}
```
</p>
</details>