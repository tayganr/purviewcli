# pv entity create
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > create

## Description
Create or update an entity in Atlas. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName.

## Syntax
```
pv entity create --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/create-or-update)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity
```

## Examples
Create or update an entity.

```powershell
pv entity create --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "entity": {
        "attributes": {
            "description": "This is a long description.",
            "name": "myfile.csv",
            "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/myfile.csv",
            "isFile": true
        },
        "collectionId": "esg-26fa7f24-pv",
        "typeName": "azure_datalake_gen2_path"
    }
}
```
</p>
</details><br />
Create an entity with custom attributes.

```powershell
pv entity create --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "entity": {
        "attributes": {
            "description": "This is a long description.",
            "name": "myfile.csv",
            "qualifiedName": "https://storage_account.dfs.core.windows.net/01-bronze/folder/file.csv",
            "isFile": true
        },
        "customAttributes": {
            "custAttr1": "hello",
            "custAttr2": "world"
        },
        "collectionId": "rqbhvc",
        "typeName": "azure_datalake_gen2_path"
    }
}
```
</p>