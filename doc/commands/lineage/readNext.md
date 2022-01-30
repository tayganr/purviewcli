# pv lineage readNext
[Command Reference](../../../README.md#command-reference) > [lineage](./main.md) > readNext

## Description
Return immediate next page lineage info about entity with pagination.

## Syntax
```
pv lineage readNext --guid=<val> [--direction<val> --offset=<val> --limit=<val>]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity. This needs to be a valid lineage entity type (e.g. adf_copy_operation).

## Optional Arguments
`--direction` (string)  
The direction of the lineage, which could be INPUT, OUTPUT or BOTH.

`--offset` (integer)  
The offset for pagination purpose.

`--limit` (integer)  
The page size - by default there is no paging.

## API Mapping
Catalog Data Plane > Lineage > [Next Page Lineage](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/lineage/next-page-lineage)
```
GET https://{accountName}.purview.azure.com/catalog/api/lineage/{guid}/next
```

## Examples
Get lineage information for a particular entity.
```powershell
pv lineage readNext --guid "c15f00b1-bf72-4413-9e95-565be22d18ed"
```