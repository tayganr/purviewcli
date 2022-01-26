# pv glossary deleteTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > deleteTermsAssignedEntities

## Description
Delete the term assignment for the given list of related objects.

## Syntax
```
pv glossary deleteTermsAssignedEntities --termGuid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Catalog Data Plane > Glossary > Delete Term Assignment From Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/delete-term-assignment-from-entities)
```
DELETE https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
```powershell

```