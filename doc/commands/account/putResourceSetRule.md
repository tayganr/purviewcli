# pv account putResourceSetRule
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > putResourceSetRule

## Description
Creates or updates a resource set.

## Syntax
```
pv account putResourceSetRule --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Resource Set Rules > [Create Or Update Resource Set Rule](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/resource-set-rules/create-or-update-resource-set-rule)
```
PUT https://{accountName}.purview.azure.com/account/resourceSetRuleConfigs/defaultResourceSetRuleConfig
```

## Examples
Create or update a resource set.
```powershell
pv account putResourceSetRule --payloadFile "/path/to/file.json"
```