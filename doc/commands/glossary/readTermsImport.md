# pv glossary readTermsImport
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsImport

## Description
Get the status of import csv operation

## Syntax
```
pv glossary readTermsImport --operationGuid=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > Get Import Csv Operation Status](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-import-csv-operation-status)
```
GET https://{accountName}.purview.azure.com/catalog/api/glossary/terms/import/{operationGuid}
```

## Examples
```powershell

```