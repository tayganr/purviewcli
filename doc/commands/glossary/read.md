# pv glossary read
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > read

## Description
Get all glossaries registered with Atlas.

## Syntax
```
pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > List Glossaries](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-glossaries)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary
```

## Examples
```powershell

```