# pv entity deleteUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteUniqueAttribute

## Description
Delete an entity identified by its type and unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:<attrName>=<attrValue>. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

## Syntax
```
pv entity deleteUniqueAttribute --typeName=<val> --qualifiedName=<val>
```

## Required Arguments
`--typeName` (string)  
The name of the type.

`--qualifiedName` (string)  
The qualified name of the entity.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete By Unique Attribute](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-by-unique-attribute)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}
```

## Examples
Delete an existing entity by its type name and qualified name.
```powershell
pv entity deleteUniqueAttribute --typeName "azure_datalake_gen2_path" --qualifiedName "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/filename.csv"
```