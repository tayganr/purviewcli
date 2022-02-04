# pv types readTermTemplateDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTermTemplateDef

## Description
Get the term template definition for the given GUID or by its name (unique).

## Syntax
```
pv types readTermTemplateDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the term template.

`--name` (string)  
The name of the term template.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Term Template Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-term-template-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/types/termtemplatedef/guid/{guid}
```

Catalog Data Plane > Types > [Get Term Template Def By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-term-template-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/types/termtemplatedef/name/{name}
```

## Examples
Get term template definition by name.
```powershell
pv types readTermTemplateDef --name "My Custom Term Template"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "attributeDefs": [
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isOptional": true,
            "isUnique": false,
            "name": "Department",
            "options": {
                "isDisabled": "false"
            },
            "typeName": "TERM_TEMPLATE_ENUM_6dc2fde0_c41a_4dfa_b77e_5d20275decc5",
            "valuesMaxCount": 1,
            "valuesMinCount": 0
        }
    ],
    "category": "TERM_TEMPLATE",
    "createTime": 1643991602788,
    "createdBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
    "description": "This is a long description.",
    "guid": "71ee745e-5a99-3b0f-9e46-ed75b67c224d",
    "lastModifiedTS": "1",
    "name": "My Custom Term Template",
    "typeVersion": "1.0",
    "updateTime": 1643991602788,
    "updatedBy": "095354ff-cae8-44ff-8120-22ec5a941b40",
    "version": 1
}
```
</p>
</details>

Get term template definition by guid.
```powershell
pv types readTermTemplateDef --guid "71ee745e-5a99-3b0f-9e46-ed75b67c224d"
```