# pv entity deleteBulk
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > deleteBulk

## Description
Delete a list of entities in bulk identified by their GUIDs or unique attributes.

## Syntax
```
pv entity deleteBulk --guid=<val>...
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Delete By Guids](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/delete-by-guids)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk
```

## Examples
Delete a list of existing entities by their GUID.
```powershell
pv entity deleteBulk --guid "0d42ecc0-0fb4-4276-96b0-0561cae3e97d" --guid "31aae3f9-6d6e-4417-97f4-08d89e360d49" --guid "5b7b5ae2-e2af-46b5-8998-926e7b4ba3f9" 
```