# pv entity put
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > put

## Description
Update entity partially - create or update entity attribute identified by its GUID. Supports only primitive attribute type and entity references. It does not support updating complex types like arrays, and maps. Null updates are not possible.

## Syntax
```
pv entity put --guid=<val> --attrName=<val> --attrValue=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Partial Update Entity Attribute By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/partial-update-entity-attribute-by-guid)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}
```

## Examples
```powershell

```