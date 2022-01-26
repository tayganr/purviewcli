# pv entity putUniqueAttribute
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > putUniqueAttribute

## Description
Update entity partially - Allow a subset of attributes to be updated on an entity which is identified by its type and unique attribute  eg: Referenceable.qualifiedName. Null updates are not possible. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

## Syntax
```
pv entity putUniqueAttribute --typeName=<val> --payload-file=<val>
```

## Required Arguments
`--typeName` (type)  
Description

`--payload-file` (type)  
Description

## Optional Arguments
*None*

## Examples
```powershell

```