# pv credential put
[Command Reference](../../../README.md#command-reference) > [credential](./main.md) > put

## Description
Create or update a credential.

## Syntax
```
pv scan putCredential --credentialName=<val> --payloadFile=<val>
```

## Required Arguments
`--credentialName` (string)  
The name of the credential.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Create or update a credential.
```
PUT https://{accountName}.purview.azure.com/scan/credentials/{credentialName}
```

## Examples
Create or update a credential.
```powershell
pv scan putCredential --credentialName "my_new_sql_credential"  --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "name": "my_new_sql_credential",
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
    }
}
```
</p>
</details>