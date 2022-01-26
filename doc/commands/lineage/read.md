# pv lineage read
[Command Reference](../../../README.md#command-reference) > [lineage](./main.md) > read

## Description
Get lineage info of the entity specified by GUID.

## Syntax
```
pv lineage read --guid=<val> [--depth=<val> --width=<val> --direction=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Lineage > Get Lineage Graph](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/lineage/get-lineage-graph)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/lineage/{guid}
```

## Examples
```powershell

```