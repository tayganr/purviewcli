# pv glossary createTermsImport
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTermsImport

## Description
Import Glossary Terms from local csv file

## Syntax
```
pv glossary createTermsImport (--glossaryGuid=<val> | --glossaryName=<val>)
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Import Glossary Terms Via Csv](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/import-glossary-terms-via-csv)
```
POST https://{accountName}.purview.azure.com/catalog/api/glossary/{glossaryGuid}/terms/import
```

## Examples
```powershell

```