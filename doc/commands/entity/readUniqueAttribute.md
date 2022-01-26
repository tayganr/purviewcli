# pv entity readUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readUniqueAttribute

## Description
Get complete definition of an entity given its type and unique attribute. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:<attrName>=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

## Syntax
```
pv entity readUniqueAttribute --typeName=<val> --qualifiedName=<val> [--ignoreRelationships --minExtInfo]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Entity > Get By Unique Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-by-unique-attributes)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}
```

## Examples
```powershell

```