# pv entity createUniqueAttributeClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createUniqueAttributeClassifications

## Description
Add classification to the entity identified by its type and unique attributes.

## Syntax
```
pv entity createUniqueAttributeClassifications --typeName=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Add Classifications By Unique Attribute](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-classifications-by-unique-attribute)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classifications
```

## Examples
```powershell

```