# pv scan putKeyVault
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putKeyVault

## Description
Creates an instance of a key vault connection

## Syntax
```
pv scan putKeyVault --keyVaultName=<val> --payload-file=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
[Scanning Data Plane > Key Vault Connections > Create](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/key-vault-connections/create)
```
PUT https://{accountName}.purview.azure.com/scan/azureKeyVaults/{keyVaultName}
```

## Examples
```powershell

```