# pv credential put
[Command Reference](../../../README.md#command-reference) > [credential](./main.md) > put

## Description
Create or update a credential.

## Syntax
```
pv credential put --credentialName=<val> --payload-file=<val>
```

## Required Arguments
`--credentialName` (string)  
The name of the credential.

`--payload-file` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Create or update a credential.
```
PUT https://{accountName}.purview.azure.com/proxy/credentials/{credentialName}
```

## Examples
Create or update a credential.
```powershell
pv credential put --credentialName "credential-SQL" --payload-file "/Path/to/file.json"
```