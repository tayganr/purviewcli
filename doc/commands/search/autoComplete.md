# pv search autoComplete
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > autoComplete

## Description
Get auto complete options.

## Syntax
```
pv search autoComplete [--keywords=<val> --limit=<val> --filter-file=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all fields that support autocomplete operation. It must be at least 1 character, and no more than 100 characters.

`--limit` (integer)  
The number of autocomplete results we hope to return. The default value is 50. The value must be a number between 1 and 100.

`--filter-file` (string)  
The filter for the autocomplete request.

## Examples
```powershell

```