# pv share registerEmail

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  registerEmail

## Description

Registers the tenant and email combination for activation.

## Syntax

```
pv share registerEmail
```

## Required Arguments

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Email Registration > [Register](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/email-registration/register)
```
POST https://{accountName}.purview.azure.com/share/registerEmail
```

## Examples

Registers the tenant and email combination for activation.

```powershell
pv share registerEmail
```