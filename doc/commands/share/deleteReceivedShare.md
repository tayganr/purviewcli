# pv share deleteReceivedShare

[Command Reference](../../../README.md#command-reference) > [share](./main.md) >  deleteReceivedShare

## Description

Deletes a received share.

## Syntax

```
pv share deleteReceivedShare --receivedShareName=<val>
```

## Required Arguments

`--receivedShareName` (string)
The name of the received share.

## Optional Arguments

*None*

## API Mapping

Share Data Plane > Received Shares > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/received-shares/delete)
```
DELETE https://{accountName}.purview.azure.com/share/receivedShares/{receivedShareName}
```

## Examples

Delete a received share.

```powershell
pv share deleteReceivedShare --receivedShareName "NewShare"
```