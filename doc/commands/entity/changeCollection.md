# pv entity changeCollection
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > changeCollection

## Description
Move existing entities to the target collection.

## Syntax
```
pv entity changeCollection --collection=<val> --payloadFile=<val>
```

## Required Arguments
`--collection` (string)  
The collection unique name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Collection > [Move Entities To Collection](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/collection/move-entities-to-collection)
```
POST https://{accountName}.purview.azure.com/catalog/api/collections/{collection}/entity/moveHere
```

## Examples
Move a list of existing entities to a target collection.
```powershell
pv entity changeCollection --collection "tdumy6" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "entityGuids": [
      "8409533f-698b-405e-8e99-40f6f6f60000",
      "893c32e2-cfdb-4c25-bfec-d19610465d50"
    ]
}
```
</p>
</details>