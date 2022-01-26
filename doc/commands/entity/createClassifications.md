# pv entity createClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createClassifications

## Description
Add classifications to an existing entity represented by a GUID.

## Syntax
```
pv entity createClassifications --guid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Entity > Add Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-classifications)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/classifications
```

## Examples
```powershell

```