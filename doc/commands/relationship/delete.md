# pv relationship delete
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > delete

## Description
Delete a relationship between entities by its GUID.

## Syntax
```
pv relationship delete --guid=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the relationship.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Relationship > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/delete)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship/guid/{guid}
```

## Examples
Delete a relationship between entities by relationship GUID.
```powershell
pv relationship delete --guid "90ca81c2-2d68-43f6-90cc-198a0fd07548"
```