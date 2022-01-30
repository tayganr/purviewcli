# pv scan readDataSources
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readDataSources

## Description
List data sources in Data catalog.

## Syntax
```
pv scan readDataSources
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Data Sources > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/data-sources/list-all)
```
GET https://{accountName}.purview.azure.com/scan/datasources
```

## Examples
List all data sources.
```powershell
pv scan readDataSources
```