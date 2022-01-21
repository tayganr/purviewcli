# pv search browse
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > browse

## Description
Browse entities by path or entity type.

## Synopsis
```
pv search browse (--entityType=<val> | --path=<val>) [--limit=<val> --offset=<val>]
```

## Required Arguments
`--entityType` (string)  
The entity type to browse as the root level entry point.

`--path` (string)  
The path to browse the next level child entities.

## Optional Arguments
`--limit` (integer)  
The number of browse items we hope to return. The maximum value is 10000.

`--offset` (integer)  
The offset. The default value is 0. The maximum value is 100000.

## Examples
```powershell

```