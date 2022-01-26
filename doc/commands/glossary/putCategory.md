# pv glossary putCategory
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putCategory

## Description
Update the given glossary category by its GUID.

## Syntax
```
pv glossary putCategory --categoryGuid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Update Glossary Category](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/update-glossary-category)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}
```

## Examples
```powershell

```