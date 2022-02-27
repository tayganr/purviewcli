# pv scan readKeyVault
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readKeyVault

## Description
Gets key vault information

## Syntax
```
pv scan readKeyVault --keyVaultName=<val>
```

## Required Arguments
`--keyVaultName` (string)  
The name of the key vault connection.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Key Vault Connections > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/key-vault-connections/get)
```
GET https://{accountName}.purview.azure.com/scan/azureKeyVaults/{keyVaultName}
```

## Examples
Get Azure Key Vault connection information by name.
```powershell
pv scan readKeyVault --keyVaultName "my_key_vault"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "/subscriptions/2c141777-2036-4ba0-a7f4-bbca73a181bf/resourceGroups/scanning-prod-westeurope/providers/Microsoft.Purview/accounts/purview-c66c7ceb-1944-4393-ae27-20497005f353/linkedservices/my_key_vault",
    "name": "my_key_vault",
    "properties": {
        "baseUrl": "https://pvdemofngxi-keyvault.vault.azure.net/",
        "description": ""
    }
}
```
</p>
</details>