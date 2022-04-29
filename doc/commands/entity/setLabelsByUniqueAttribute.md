# pv entity setLabelsByUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > setLabelsByUniqueAttribute

## Description
Overwrite labels for an entity identified by its type and unique attributes.

## Syntax
```
pv entity setLabelsByUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
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
Catalog Data Plane > Entity > [Set labels to a given entity identified by its type and unique attributes.](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/set-labels-by-unique-attribute)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/labels
```

## Examples
Overwrite labels property for an existing entity identified by its type and unique attributes.
```powershell
pv entity setLabelsByUniqueAttribute --typeName "azure_datalake_gen2_resource_set" --qualifiedName "https://STORAGE_ACCOUNT.dfs.core.windows.net/bing/data/{N}/QueriesByCountry_{Year}-{Month}-{Day}_{N}-{N}-{N}.tsv" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
[
    "a",
    "b",
    "c"
]
```
</p>
</details>