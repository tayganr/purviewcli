# pv glossary readTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsAssignedEntities

## Description
Get all related objects assigned with the specified term.

## Syntax
```
pv glossary readTermsAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > Get Entities Assigned With Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-entities-assigned-with-term)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
```powershell

```