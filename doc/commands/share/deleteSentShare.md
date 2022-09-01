# pv share getSentShare
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > getSentShare

## Description
Deletes a sent share.

## Syntax
```
pv share deleteSentShare --sentShareName=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Share Data Plane > Sent Shares > [Delete](https://docs.microsoft.com/en-us/rest/api/purview/sharedataplane/sent-shares/delete)
```
DELETE https://{accountName}.purview.azure.com/share/sentShares/{sentShareName}
```

## Examples
Delete a sent share in the given Microsoft Purview account by specifying the share name.
```powershell
pv share deleteSentShare --sentShareName "MyShare"
```