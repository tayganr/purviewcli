# pv entity createBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createBulk

## Description
Create or update entities in Atlas in bulk. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName.

## Syntax
```
pv entity createBulk --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Create Or Update Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/create-or-update-entities)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk
```

## Examples
Create or update entities in bulk.
```powershell
pv entity createBulk --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "entities": [
        {
            "attributes": {
                "description": "This is a long description.",
                "name": "myfile01.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/myfile01.csv",
                "isFile": true
            },
            "collectionId": "esg-26fa7f24-pv",
            "typeName": "azure_datalake_gen2_path"
        },
        {
            "attributes": {
                "description": "This is a long description.",
                "name": "myfile02.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/myfile02.csv",
                "isFile": true
            },
            "collectionId": "esg-26fa7f24-pv",
            "typeName": "azure_datalake_gen2_path"
        },
        {
            "attributes": {
                "description": "This is a long description.",
                "name": "myfile03.csv",
                "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/myfile03.csv",
                "isFile": true
            },
            "collectionId": "esg-26fa7f24-pv",
            "typeName": "azure_datalake_gen2_path"
        }
    ]
}
```
</p>
</details>