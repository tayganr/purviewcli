# pv entity createOrUpdateCollection
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createOrUpdateCollection

## Description
Creates or updates an entity to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName.

## Syntax
```
pv entity createOrUpdateCollection --collection=<val> --payloadFile=<val>
```

## Required Arguments
`--collection` (string)  
The collection unique name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Collection > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/collection/create-or-update)
```
POST https://{accountName}.purview.azure.com/catalog/api/collections/{collection}/entity
```

## Examples
Create or update an entity to a collection.
```powershell
pv entity createOrUpdateCollection --collection "tdumy6" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
  "referredEntities": {},
  "entity": {
    "typeName": "azure_datalake_gen2_path",
    "attributes": {
      "name": "merged.parquet",
      "qualifiedName": "https://pvdemocrv3kadls.dfs.core.windows.net/bing/data/merged.parquet"
    }
  }
}
```
</p>
</details>