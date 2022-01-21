# pv search query

## Description
Gets data using search.

## Synopsis
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
The filter for the search. See examples for the usage of supported filters.

`--facets-file` (string)  
The content of a search facet result item.

## Examples
```powershell
pv search query --keywords "sales"
```