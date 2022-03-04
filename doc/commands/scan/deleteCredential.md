# pv credential delete
[Command Reference](../../../README.md#command-reference) > [credential](./main.md) > delete

## Description
Delete a credential.

## Syntax
```
pv scan deleteCredential --credentialName=<val>
```

## Required Arguments
`--credentialName` (string)  
The name of the credential.

## Optional Arguments
*None*

## API Mapping
Create or update a credential.
```
DELETE https://{accountName}.purview.azure.com/scan/credentials/{credentialName}
```

## Examples
```powershell
pv scan deleteCredential --credentialName "credential-SQL"
```