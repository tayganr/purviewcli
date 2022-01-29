# pv search browse
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > browse

## Description
Browse entities by path or entity type.

## Syntax
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

## API Mapping
Catalog Data Plane > Discovery > [Browse](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/browse)
```
POST https://{accountName}.purview.azure.com/catalog/api/browse
```

## Examples
Browse entities by entity type.
```powershell
pv search browse --entityType "azure_sql_table"
```

Browse entities by path.
```powershell
pv search browse --path "/azure_sql_server#pvlab-4da424-sqlsvr.database.windows.net/azure_sql_db#pvlab-4da424-sqldb"
```
