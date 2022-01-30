# pv glossary createTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTermsAssignedEntities

## Description
Assign the given term to the provided list of related objects.

## Syntax
```
pv glossary createTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Assign Term To Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/assign-term-to-entities)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
```powershell

```