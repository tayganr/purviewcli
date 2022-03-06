# pv insight tags
[Command Reference](../../../README.md#command-reference) > [insight](./main.md) > tags

## Description
Number of assets by tags.

## Syntax
```
pv insight tags
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
```
GET https://{accountName}.purview.azure.com/mapanddiscover/reports/serverless/asset2/tags/getSnapshot
```

## Examples
Get the number of assets by tags.
```powershell
pv insight tags
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "records": [
        {
            "files": 0,
            "sourceType": "Passenger_information",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "sourceType": "IoT_data",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "name": "CUSTOM_PARTS",
            "sourceType": "Azure SQL Data Warehouse",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "sourceType": "demo_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "Azure SQL Data Warehouse",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Label"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.CANADA.DRIVERS_LICENSE_NUMBER",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 1,
            "sourceType": "Azure Data Lake Storage Gen1",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "demo97_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.FINANCIAL",
            "name": "MICROSOFT.FINANCIAL.JAPAN.BANK_ACCOUNT_NUMBER",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 1,
            "group": "MICROSOFT.GOVERNMENT",
            "sourceType": "Azure Data Lake Storage Gen1",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.CHILE.CDI_NUMBER",
            "sourceType": "hive",
            "sources": 2,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "name": "manual_import",
            "sourceType": "IoT_data",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.CHILE.CDI_NUMBER",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "sourceType": "Management_data",
            "sources": 1,
            "subscriptions": 0,
            "tables": 3,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "name": "manual_import",
            "sourceType": "Passenger_information",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.FRANCE.DRIVERS_LICENSE_NUMBER",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "name": "manual_import",
            "sourceType": "Management_data",
            "sources": 1,
            "subscriptions": 0,
            "tables": 3,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "Management_data",
            "sources": 1,
            "subscriptions": 0,
            "tables": 3,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "sourceType": "Azure SQL Data Warehouse",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.FRANCE.DRIVERS_LICENSE_NUMBER",
            "sourceType": "hive",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.FINANCIAL",
            "name": "MICROSOFT.FINANCIAL.JAPAN.BANK_ACCOUNT_NUMBER",
            "sourceType": "hive",
            "sources": 2,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.NAME",
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "3",
            "sourceType": "Azure SQL Data Warehouse",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Label"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 4,
            "sourceType": "Azure Blob Storage",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Label"
        },
        {
            "files": 0,
            "sourceType": "IoT_data",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "sourceType": "demo97_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 1,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "sourceType": "Azure Data Lake Storage Gen1",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.DATE_OF_BIRTH",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 1,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.US.STATE",
            "sourceType": "Azure Data Lake Storage Gen1",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "sourceType": "hive",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "demo_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "sourceType": "hive",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 4,
            "group": "3",
            "name": "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055",
            "sourceType": "Azure Blob Storage",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Label"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.IPADDRESS",
            "sourceType": "demo_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.IPADDRESS",
            "sourceType": "demo97_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.TURKEY.TURKISH_NATIONAL_IDENTIFICATION_NUMBER",
            "sourceType": "hive",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "name": "ORDER__NUM",
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "Azure SQL Data Warehouse",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.FINANCIAL",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 4,
            "group": "3",
            "sourceType": "Azure Blob Storage",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Label"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "sourceType": "demo97_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "hive",
            "sources": 2,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "Custom",
            "sourceType": "Passenger_information",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "sourceType": "demo_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.TURKEY.TURKISH_NATIONAL_IDENTIFICATION_NUMBER",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.IPADDRESS",
            "sourceType": "demo97_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "sourceType": "hive",
            "sources": 2,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.IPADDRESS",
            "sourceType": "demo_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.HONGKONG.ID_CARD_NUMBER",
            "sourceType": "demo_column",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "sourceType": "Azure SQL Database",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 1,
            "group": "MICROSOFT.GOVERNMENT",
            "name": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "sourceType": "Azure Data Lake Storage Gen1",
            "sources": 1,
            "subscriptions": 1,
            "tables": 0,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "3",
            "name": "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055",
            "sourceType": "Azure SQL Data Warehouse",
            "sources": 1,
            "subscriptions": 1,
            "tables": 1,
            "type": "Label"
        },
        {
            "files": 0,
            "group": "MICROSOFT.FINANCIAL",
            "sourceType": "hive",
            "sources": 2,
            "subscriptions": 0,
            "tables": 2,
            "type": "Classification"
        },
        {
            "files": 0,
            "group": "MICROSOFT.PERSONAL",
            "name": "MICROSOFT.PERSONAL.DATE_OF_BIRTH",
            "sourceType": "hive",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        },
        {
            "files": 0,
            "sourceType": "demo97_table",
            "sources": 1,
            "subscriptions": 0,
            "tables": 1,
            "type": "Classification"
        }
    ],
    "snapshotTime": "2022-01-26T00:00:00Z"
}
```
</p>
</details>
