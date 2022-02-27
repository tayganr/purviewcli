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
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "value": [
        {
            "id": "/subscriptions/2c141777-2036-4ba0-a7f4-bbca73a181bf/resourceGroups/scanning-prod-westeurope/providers/Microsoft.Purview/accounts/purview-c66c7ceb-1944-4393-ae27-20497005f353/linkedservices/my_key_vault",
            "name": "my_key_vault",
            "properties": {
                "baseUrl": "https://pvdemofngxi-keyvault.vault.azure.net/",
                "description": ""
            }
        },
        {
            "id": "/subscriptions/2c141777-2036-4ba0-a7f4-bbca73a181bf/resourceGroups/scanning-prod-westeurope/providers/Microsoft.Purview/accounts/purview-c66c7ceb-1944-4393-ae27-20497005f353/linkedservices/My Key Vault",
            "name": "My Key Vault",
            "properties": {
                "baseUrl": "https://mykv-keyvault.vault.azure.net/",
                "description": ""
            }
        }
    ]
}
```
</p>
</details>