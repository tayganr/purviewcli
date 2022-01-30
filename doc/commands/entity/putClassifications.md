# pv entity putClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > putClassifications

## Description
Update classifications to an existing entity represented by a guid.

## Syntax
```
pv entity putClassifications --guid=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Update Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/update-classifications)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classifications
```

## Examples
```powershell

```