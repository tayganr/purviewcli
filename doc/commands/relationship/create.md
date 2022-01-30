# pv relationship create
[Command Reference](../../../README.md#command-reference) > [relationship](./main.md) > create

## Description
Create a new relationship between entities.

## Syntax
```
pv relationship create --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Relationship > [Create](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/relationship/create)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/relationship
```

## Examples
Create a new relationship.
```powershell
pv relationship create --payloadFile "/path/to/file.json"
```