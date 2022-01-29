# pv credential delete
[Command Reference](../../../README.md#command-reference) > [credential](./main.md) > delete

## Description
Delete a credential.

## Syntax
```
pv credential delete --credentialName=<val>
```

## Required Arguments
`--credentialName` (string)  
The name of the credential.

## Optional Arguments
*None*

## API Mapping
Create or update a credential.
```
DELETE https://{accountName}.purview.azure.com/proxy/credentials/{credentialName}
```

## Examples
```powershell
pv credential delete --credentialName "credential-SQL"
```