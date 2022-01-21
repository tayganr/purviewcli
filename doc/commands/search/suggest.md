# pv search suggest

## Description
Get search suggestions by query criteria.

## Synopsis
```
pv search suggest [--keywords=<val> --limit=<val> --filter-file=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all fields that support suggest operation. It must be at least 1 character, and no more than 100 characters. In the index schema we defined a default suggester which lists all the supported fields and specifies a search mode.

`--limit` (integer)  
The number of suggestions we hope to return. The default value is 5. The value must be a number between 1 and 100.

`--filter-file` (string)  
The filter for the search.

## Examples
```powershell

```