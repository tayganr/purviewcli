# pv entity createOrUpdateCollectionBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createOrUpdateCollectionBulk

## Description
Creates or updates entities in bulk to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName.

## Syntax
```
pv entity createOrUpdateCollectionBulk --collection=<val> --payloadFile=<val>
```

## Required Arguments
`--collection` (string)  
The collection unique name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Collection > [Create Or Update Bulk](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/collection/create-or-update-bulk)
```
POST https://{accountName}.purview.azure.com/catalog/api/collections/{collection}/entity/bulk
```

## Examples
Create or update entities in bulk to a collection.
```powershell
pv entity createOrUpdateCollectionBulk --collection "tdumy6" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "referredEntities": {},
    "entities": [
        {
            "typeName": "azure_datalake_gen2_path",
            "attributes": {
                "name": "merged.parquet",
                "qualifiedName": "https://pvdemocrv3kadls.dfs.core.windows.net/bing/data/merged.parquet"
            }
        },
        {
            "typeName": "azure_datalake_gen2_path",
            "attributes": {
                "name": "twitter_handles.parquet",
                "qualifiedName": "https://pvdemocrv3kadls.dfs.core.windows.net/twitter/twitter_handles.parquet"
            }
        }
    ]
}
```
</p>
</details>