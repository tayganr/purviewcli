# pv entity putUniqueAttributeClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > putUniqueAttributeClassifications

## Description
Update classification on an entity identified by its type and unique attributes.

## Syntax
```
pv entity putUniqueAttributeClassifications --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
```

## Required Arguments
`--typeName` (string)  
The name of the type.

`--qualifiedName` (string)  
The qualified name of the entity.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Update Classifications By Unique Attribute](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/update-classifications-by-unique-attribute)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classifications
```

## Examples
```powershell
pv entity putUniqueAttributeClassifications --typeName "azure_datalake_gen2_filesystem" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/02-silver" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "typeName": "MICROSOFT.FINANCIAL.CREDIT_CARD_NUMBER",
        "attributes": {
            "confidence": 7
        }
    }
]
```
</p>
</details>