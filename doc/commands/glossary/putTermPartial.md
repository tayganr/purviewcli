# pv glossary putTermPartial
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putTermPartial

## Description
Update the glossary term partially.

## Syntax
```
pv glossary putTermPartial --termGuid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Partial Update Glossary Term](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/partial-update-glossary-term)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/term/{termGuid}/partial
```

## Examples
```powershell

```