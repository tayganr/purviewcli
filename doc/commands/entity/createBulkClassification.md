# pv entity createBulkClassification
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createBulkClassification

## Description
Associate a classification to multiple entities in bulk.

## Syntax
```
pv entity createBulkClassification --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Entity > Add Classification](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/add-classification)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk/classification
```

## Examples
```powershell

```