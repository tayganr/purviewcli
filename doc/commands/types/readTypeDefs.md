# pv types readTypeDefs
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTypeDefs

## Description
Get all type definitions in Atlas in bulk.

## Syntax
```
pv types readTypeDefs [--includeTermTemplate --type=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--includeTermTemplate` (boolean)  
Whether to include termtemplatedef when returning all typedefs. Default: false.

`--type` (string)  
Restrict results to a specific type of type definition (classification | entity | enum | relationship | struct | term_template).

## API Mapping
Catalog Data Plane > Types > [Get All Type Definitions](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-all-type-definitions)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

## Examples
```powershell

```