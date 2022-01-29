# pv credential read
[Command Reference](../../../README.md#command-reference) > [credential](./main.md) > read

## Description
Get a credential.

## Syntax
```
pv credential read [--credentialName=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--credentialName` (string)  
The name of the credential.

## API Mapping
Get all credentials.
```
GET https://{accountName}.purview.azure.com/proxy/credentials
```

Get a credential by name.
```
GET https://{accountName}.purview.azure.com/proxy/credentials/{credentialName}
```

## Examples
Get all credentials.
```powershell
pv credential read
```

Get a credential by name.
```powershell
pv credential read --credentialName "credential-SQL"
```
