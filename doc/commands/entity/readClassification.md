# pv entity readClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readClassification

## Description
Get a classification assigned for a given entity by the entity GUID and classification name.

## Syntax
```
pv entity readClassification --guid=<val> --classificationName=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

`--classificationName` (string)  
The name of the classification.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Classification](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-classification)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classification/{classificationName}
```

## Examples
Get a classification assigned to a particular entity via the entity GUID and classification name.
```powershell
pv entity readClassification --guid "c6a7811a-0699-44d0-b0be-68babe560ab2" --classificationName "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "attributes": {
        "confidence": null
    },
    "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
    "entityStatus": "ACTIVE",
    "lastModifiedTS": "1",
    "typeName": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER"
}
```
</p>
</details>