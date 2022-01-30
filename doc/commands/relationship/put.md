# pv relationship put
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > put

## Description
Update an existing relationship between entities.

## Syntax
```
pv relationship put --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Relationship > [Update](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/update)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship
```

## Examples
Update an existing relationship.
```powershell
pv relationship put --payloadFile "/path/to/file.json"
```