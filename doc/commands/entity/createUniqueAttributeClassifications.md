# pv entity createUniqueAttributeClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createUniqueAttributeClassifications

## Description
Add classification to the entity identified by its type and unique attributes.

## Syntax
```
pv entity createUniqueAttributeClassifications --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
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
Catalog Data Plane > Entity > [Add Classifications By Unique Attribute](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-classifications-by-unique-attribute)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classifications
```

## Examples
Associate an entity to multiple classifications via a unique attribute (e.g. qualifiedName).
```powershell
pv entity createUniqueAttributeClassifications --typeName "azure_datalake_gen2_filesystem" --qualifiedName  "https://esg26fa7f24adls.dfs.core.windows.net/02-silver" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    {
        "typeName": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
    },
    {
        "typeName": "MICROSOFT.FINANCIAL.CREDIT_CARD_NUMBER"
    }
]
```
</p>
</details>