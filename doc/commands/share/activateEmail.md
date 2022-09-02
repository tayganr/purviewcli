# pv share activateEmail

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  activateEmail

## Description

Activates the tenant and email combination using the activation code received.

## Syntax

```
pv share activateEmail --payloadFile=<val>
```

## Required Arguments

`--payloadFile` (string)

File path to a valid JSON document.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Email Registration > [Activate](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/email-registration/activate)

```
POST https://{accountName}.purview.azure.com/share/activateEmail
```

## Examples

Description
```powershell
pv share _EXAMPLE_
```


<details><summary>Sample response.</summary>
<p>

```json
{
    "key": "value"
}
```
</p>
</details>
