# pv lineage readNext
[Command Reference](../../../README.md#command-reference) > [lineage](./main.md) > readNext

## Description
Return immediate next page lineage info about entity with pagination

## Syntax
```
pv lineage readNext --guid=<val> [--direction<val> --offset=<val> --limit=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Lineage > Next Page Lineage](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/lineage/next-page-lineage)
```
GET https://{accountName}.purview.azure.com/catalog/api/lineage/{guid}/next
```

## Examples
```powershell

```