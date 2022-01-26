# pv glossary putTermsAssignedEntities
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putTermsAssignedEntities

## Description
Delete the term assignment for the given list of related objects.

## Syntax
```
pv glossary putTermsAssignedEntities --termGuid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Remove Term Assignment From Entities](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/remove-term-assignment-from-entities)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/terms/{termGuid}/assignedEntities
```

## Examples
```powershell

```