# pv scan putKeyVault
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putKeyVault

## Description
Creates an instance of a key vault connection

## Syntax
```
pv scan putKeyVault --keyVaultName=<val> --payloadFile=<val>
```

## Required Arguments
`--keyVaultName` (string)  
The key vault connection name.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Key Vault Connections > [Create](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/key-vault-connections/create)
```
PUT https://{accountName}.purview.azure.com/scan/azureKeyVaults/{keyVaultName}
```

## Examples
Create a key vault connection.
```powershell
pv scan putKeyVault --keyVaultName "My Key Vault" --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "name": "My Key Vault",
    "properties": {
        "baseUrl": "https://mykv-keyvault.vault.azure.net/",
        "description": ""
    }
}
```
</p>
</details>