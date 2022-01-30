# pv relationship read
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > read

## Description
Get relationship information between entities by its GUID.

## Syntax
```
pv relationship read --guid=<val> [--extendedInfo]
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the relationship.

## Optional Arguments
`--extendedInfo` (boolean)  
Limits whether includes extended information.

## API Mapping
Catalog Data Plane > Relationship > [Get](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/get)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship/guid/{guid}
```

## Examples
Get relationship information between entities by relationship GUID.
```powershell
pv relationship read --guid "90ca81c2-2d68-43f6-90cc-198a0fd07548"
```

Include extended information (e.g. referredEntities).
```powershell
pv relationship read --guid "90ca81c2-2d68-43f6-90cc-198a0fd07548" --extendedInfo
```