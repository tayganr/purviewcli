# pv types readTypeDefsHeaders
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readTypeDefsHeaders

## Description
List all type definitions returned as a list of minimal information header.

## Syntax
```
pv types readTypeDefsHeaders [--includeTermTemplate --type=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--includeTermTemplate` (boolean)  
Whether to include termtemplatedef when returning all typedefs. Default: false.

`--type` (string)  
Restrict results to a specific type of type definition (classification | entity | enum | relationship | struct | term_template).

## API Mapping
Catalog Data Plane > Types > [List Type Definition Headers](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/list-type-definition-headers)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedefs/headers
```

## Examples
```powershell

```