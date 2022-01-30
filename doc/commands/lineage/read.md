# pv lineage read
[Command Reference](../../../README.md#command-reference) > [lineage](./main.md) > read

## Description
Get lineage info of the entity specified by GUID.

## Syntax
```
pv lineage read --guid=<val> [--depth=<val> --width=<val> --direction=<val>]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity. This needs to be a valid lineage entity type (e.g. adf_copy_operation).

## Optional Arguments
`--depth` (integer)  
The number of hops for lineage.

`--width` (integer)  
The number of max expanding width in lineage.

`--direction` (string)  
The direction of the lineage, which could be INPUT, OUTPUT or BOTH.

## API Mapping
Catalog Data Plane > Lineage > [Get Lineage Graph](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/lineage/get-lineage-graph)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/lineage/{guid}
```

## Examples
Get lineage information for a particular entity.
```powershell
pv lineage read --guid "c15f00b1-bf72-4413-9e95-565be22d18ed"
```