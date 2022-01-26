# pv types readTermTemplateDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTermTemplateDef

## Description
Get the term template definition for the given GUID.

## Syntax
```
pv types readTermTemplateDef (--guid=<val> | --name=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Term Template Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-term-template-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/types/termtemplatedef/guid/{guid}
```

## Examples
```powershell

```