# pv scan readKeyVaults
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readKeyVaults

## Description
List Azure Key Vault connections.

## Syntax
```
pv scan readKeyVaults
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Key Vault Connections > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/key-vault-connections/list-all)
```
GET https://{accountName}.purview.azure.com/scan/azureKeyVaults
```

## Examples
List Azure Key Vault connections.
```powershell
pv scan readKeyVaults
```