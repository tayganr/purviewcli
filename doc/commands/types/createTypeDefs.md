# pv types createTypeDefs
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > createTypeDefs

## Description
Create all atlas type definitions in bulk, only new definitions will be created. Any changes to the existing definitions will be discarded.

## Syntax
```
pv types createTypeDefs --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Create Type Definitions](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/create-type-definitions)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

## Examples
```powershell

```