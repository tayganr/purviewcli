# pv types readClassificationDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readClassificationDef

## Description
Get the classification definition for the given GUID or by its name (unique).

## Syntax
```
pv types readClassificationDef (--guid=<val> | --name=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Classification Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-classification-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/classificationdef/guid/{guid}
```

Catalog Data Plane > Types > [Get Classification Def By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-classification-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/classificationdef/name/{name}
```

## Examples
```powershell

```