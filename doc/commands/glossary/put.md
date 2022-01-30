# pv glossary put
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > put

## Description
Update the given glossary.

## Syntax
```
pv glossary put --glossaryGuid=<val> --payloadFile=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Update Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/update-glossary)
```
PUT https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}
```

## Examples
```powershell

```