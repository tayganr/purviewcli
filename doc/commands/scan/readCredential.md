# pv credential read
[Command Reference](../../../README.md#command-reference) > [credential](./main.md) > read

## Description
Get a credential.

## Syntax
```
pv scan readCredential [--credentialName=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--credentialName` (string)  
The name of the credential.

## API Mapping
Get all credentials.
```
GET https://{accountName}.purview.azure.com/scan/credentials
```

Get a credential by name.
```
GET https://{accountName}.purview.azure.com/scan/credentials/{credentialName}
```

## Examples
Get all credentials.
```powershell
pv scan readCredential
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "value": [
        {
            "etag": "1902bb63-0000-0d00-0000-621b7a0a0000",
            "id": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/scanning-prod-westeurope/providers/Microsoft.Purview/accounts/YOUR_PURVIEW_ACCOUNT/credentials/basic_credential",
            "name": "basic_credential",
            "properties": {
                "type": "BasicAuth",
                "typeProperties": {
                    "password": {
                        "secretName": "my-secret-name",
                        "secretVersion": "",
                        "store": {
                            "referenceName": "my_key_vault",
                            "type": "LinkedServiceReference"
                        },
                        "type": "AzureKeyVaultSecret"
                    },
                    "user": "username"
                }
            },
            "type": "Microsoft.Purview/accounts/credentials"
        },
        {
            "etag": "19026b66-0000-0d00-0000-621b7a290000",
            "id": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/scanning-prod-westeurope/providers/Microsoft.Purview/accounts/YOUR_PURVIEW_ACCOUNT/credentials/sql_auth",
            "name": "sql_auth",
            "properties": {
                "type": "SqlAuth",
                "typeProperties": {
                    "password": {
                        "secretName": "sql-secret-name",
                        "secretVersion": "",
                        "store": {
                            "referenceName": "my_key_vault",
                            "type": "LinkedServiceReference"
                        },
                        "type": "AzureKeyVaultSecret"
                    },
                    "user": "sql-user-name"
                }
            },
            "type": "Microsoft.Purview/accounts/credentials"
        }
    ]
}
```
</p>
</details>

Get a credential by name.
```powershell
pv credential read --credentialName "basic_credential"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "etag": "1902bb63-0000-0d00-0000-621b7a0a0000",
    "id": "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/scanning-prod-westeurope/providers/Microsoft.Purview/accounts/YOUR_PURVIEW_ACCOUNT/credentials/basic_credential",
    "name": "basic_credential",
    "properties": {
        "type": "BasicAuth",
        "typeProperties": {
            "password": {
                "secretName": "my-secret-name",
                "secretVersion": "",
                "store": {
                    "referenceName": "my_key_vault",
                    "type": "LinkedServiceReference"
                },
                "type": "AzureKeyVaultSecret"
            },
            "user": "username"
        }
    },
    "type": "Microsoft.Purview/accounts/credentials"
}
```
</p>
</details>
