# pv glossary putPartial
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > putPartial

## Description
Update the glossary partially. Some properties such as qualifiedName are not allowed to be updated.

## Syntax
```
pv glossary putPartial --glossaryGuid=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Partial Update Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/partial-update-glossary)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/partial
```

## Examples
```powershell

```