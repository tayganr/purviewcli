# pv entity createBulkSetClassifications
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > createBulkSetClassifications

## Description
Set classifications on entities in bulk.

## Syntax
```
pv entity createBulkSetClassifications --payloadFile=<val>
```

## Required Arguments
`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Set Classifications](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/set-classifications)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/bulk/setClassifications
```

## Examples
Associate sets of classifications to entities in bulk.
```powershell
pv entity createBulkSetClassifications --payloadFile "/path/to/file.json"
```
<details><summary>Example payload.</summary>
<p>

```json
{
    "guidHeaderMap": {
        "88bd838b-41a4-4644-afe8-e2fbdfc60441": {
            "attributes": {
                "qualifiedName": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourcegroups/esg/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_def"
            },
            "typeName": "ads_share_subscription",
            "classifications": [
                {
                    "typeName": "MICROSOFT.GOVERNMENT.AUSTRALIA.PASSPORT_NUMBER"
                },
                {
                    "typeName": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER"
                }
            ]
        },
        "48962df1-534d-4151-9e93-7369f33e550e": {
            "attributes": {
                "qualifiedName": "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourcegroups/esg_company_03/providers/Microsoft.DataShare/accounts/esg-26fa7f24-ds/shareSubscriptions/share_company_def/snapshots/9abd57ca-a744-4c96-acdb-5972024f0daf"
            },
            "typeName": "ads_received_snapshot",
            "classifications": [
                {
                    "typeName": "MICROSOFT.PERSONAL.IPADDRESS"
                },
                {
                    "typeName": "MICROSOFT.PERSONAL.EMAIL"
                },
                {
                    "typeName": "MICROSOFT.PERSONAL.NAME"
                }
            ]
        }
    }
}
```
</p>
</details>