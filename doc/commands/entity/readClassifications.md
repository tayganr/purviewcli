# pv entity readClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readClassifications

## Description
List classifications for a given entity represented by a GUID.

## Syntax
```
pv entity readClassifications --guid=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-classifications)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classifications
```

## Examples
Get a list of all classifications assigned to a particular entity via the entity GUID and classification name.
```powershell
pv entity readClassifications --guid "c6a7811a-0699-44d0-b0be-68babe560ab2"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "list": [
        {
            "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "entityStatus": "ACTIVE",
            "lastModifiedTS": "1",
            "source": "LabelService",
            "typeName": "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055"
        },
        {
            "attributes": {
                "confidence": null
            },
            "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "entityStatus": "ACTIVE",
            "lastModifiedTS": "1",
            "typeName": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER"
        },
        {
            "attributes": {
                "confidence": null
            },
            "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "entityStatus": "ACTIVE",
            "lastModifiedTS": "1",
            "typeName": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER"
        },
        {
            "attributes": {
                "certifiedBy": "Taygan Rifat",
                "endorsement": "Certified"
            },
            "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "entityStatus": "ACTIVE",
            "lastModifiedTS": "2",
            "typeName": "MICROSOFT.POWERBI.ENDORSEMENT"
        },
        {
            "attributes": {
                "confidence": null
            },
            "entityGuid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
            "entityStatus": "ACTIVE",
            "lastModifiedTS": "1",
            "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
        }
    ],
    "pageSize": 5,
    "sortType": "NONE",
    "startIndex": 0,
    "totalCount": 5
}
```
</p>
</details>