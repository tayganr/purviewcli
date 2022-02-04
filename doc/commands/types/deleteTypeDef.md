# pv types deleteTypeDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > deleteTypeDef

## Description
Delete API for type identified by its name.

## Syntax
```
pv types deleteTypeDef --name=<val>
```

## Required Arguments
`--name` (string)  
The name of the type.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Delete Type By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/delete-type-by-name)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/typedef/name/{name}
```

## Examples
Delete a type definition by name.
```powershell
pv types deleteTypeDef --name "My Custom Term Template"
```