# pv entity readBulkUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readBulkUniqueAttribute

## Description
Bulk API to retrieve list of entities identified by its unique attributes.

## Syntax
```
pv entity readBulkUniqueAttribute --typeName=<val> [--ignoreRelationships --minExtInfo]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Entity > Get Entities By Unique Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-entities-by-unique-attributes)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk/uniqueAttribute/type/{typeName}
```

## Examples
```powershell

```