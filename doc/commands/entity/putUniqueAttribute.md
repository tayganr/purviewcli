# pv entity putUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > putUniqueAttribute

## Description
Update entity partially - Allow a subset of attributes to be updated on an entity which is identified by its type and unique attribute  eg: Referenceable.qualifiedName. Null updates are not possible. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

## Syntax
```
pv entity putUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
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
Catalog Data Plane > Entity > [Partial Update Entity By Unique Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/partial-update-entity-by-unique-attributes)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}
```

## Examples
Update an existing entity by referring to the entities type name and qualified name.
```powershell
pv entity putUniqueAttribute --typeName "azure_datalake_gen2_path" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/myfile01.csv" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "entity": {
      "status": "ACTIVE",
      "attributes": {
        "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/myfile01.csv",
        "name": "ExampleNewName",
        "description": "This is a long description."
      },
      "typeName": "azure_storage_account"
    }
  }
```
</p>
</details>