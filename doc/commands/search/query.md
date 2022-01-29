# pv search query
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > query

## Description
Gets data using search.

## Syntax
```
pv search query [--keywords=<val> --limit=<val> --offset=<val> --filter-file=<val> --facets-file=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all searchable fields.

`--limit` (integer)  
The limit of the number of the search result. default value is 50; maximum value is 1000.

`--offset` (integer)  
The offset. The default value is 0. The maximum value is 100000.

`--filter-file` (string)  
The filter for the search.

`--facets-file` (string)  
The content of a search facet result item.

## API Mapping
Catalog Data Plane > Discovery > [Query](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/query)
```
POST https://{accountName}.purview.azure.com/catalog/api/search/query
```

## Examples
Search without specifying a keyword.
```powershell
pv search query
```

Search by keyword.
```powershell
pv search query --keywords "State"
```