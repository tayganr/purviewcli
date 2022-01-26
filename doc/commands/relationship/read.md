# pv relationship read
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > read

## Description
Get relationship information between entities by its GUID.

## Syntax
```
pv relationship read --guid=<val> [--extendedInfo]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Relationship > [Get](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/get)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship/guid/{guid}
```

## Examples
```powershell

```