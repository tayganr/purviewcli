# pv insight assetDistribution
[Command Reference](../../../README.md#command-reference) > [insight](./main.md) > assetDistribution

## Description
Asset distribution by sourceType, classificationCategory, and classification.

## Syntax
```
pv insight assetDistribution
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
```
GET https://{accountName}.purview.azure.com/mapanddiscover/reports/serverless/asset2/assetDistribution/getSnapshot
```

## Examples
Get asset distribution.
```powershell
pv insight assetDistribution
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "records": [
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 2,
            "path": "/providers/Microsoft.DataShare/tenants/",
            "sourceType": "Azure Data Share"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "https://fabrikamdwadls.core.windows.net/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 2,
            "path": "cassandra://10.5.0.4:9042/",
            "sourceType": "Cassandra"
        },
        {
            "count": 1,
            "path": "https://synapsestorageadrm.core.windows.net/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Custom",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 4,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "count": 3,
            "path": "https://app.powerbi.com/groups/657d261d-247b-4234-9c2d-515b0bbdd328/datasets/",
            "sourceType": "Power BI"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Profisee MDM"
        },
        {
            "count": 1,
            "path": "pyapacheatlas://demo_update_lineage_output/",
            "sourceType": "hive"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 13,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-month/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 10,
            "sourceType": "Azure Data Share"
        },
        {
            "count": 1,
            "path": "postgresql://fabrikam-azdb-postgresql.postgres.database.azure.com/postgres/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classificationCategory": "Security",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 2,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourcegroups/jife-rg/providers/Microsoft.DataShare/accounts/",
            "sourceType": "Azure Data Share"
        },
        {
            "count": 1,
            "path": "https://fabrikamdwadls.core.windows.net/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 3,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "AB_Custom_Classifications",
            "classificationCategory": "Custom",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.DATE_OF_BIRTH",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "https://clientdemostorage.core.windows.net/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "default.uploadadotickets_2021_09_28_080427_csv@adb-5930284167956506.6.azuredatabricks.net",
            "sourceType": "hive"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.PERSONAL.AGE",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 7,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SrcTable03#Src_c05",
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 4,
            "sourceType": "SQL Server"
        },
        {
            "count": 90,
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "https://profiseepurview.profisee.biz/",
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 9,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-combo/2020/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 1,
            "path": "Stored_Proc:Do_Something@derived_column:dest_c101_express",
            "sourceType": "demo_column_lineage"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 9,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-defaultrs/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Personal",
            "count": 2,
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.SECURITY.COMMON_PASSWORDS",
            "classificationCategory": "Security",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "mssql://azdemosrv01.database.windows.net/",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 2,
            "path": "mysql://fabrikam-azdb-mysql.mysql.database.azure.com/",
            "sourceType": "Azure Database for MySQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 2,
            "path": "https://app.powerbi.com/groups/be3b3a7d-5908-4773-920b-99e9a16befef/reports/",
            "sourceType": "Power BI"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 1,
            "path": "TgtTable02#dest_c04_express",
            "sourceType": "demo_column"
        },
        {
            "count": 1,
            "path": "mssql://ninjasql.database.windows.net/",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "mssql://azdemosrv01.database.windows.net/",
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/",
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "count": 5,
            "sourceType": "SQL Server Integration Services"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 2,
            "path": "https://fabrikamaribancosmosdb.documents.azure.com/dbs/ToDoList",
            "sourceType": "Azure Cosmos DB"
        },
        {
            "count": 10,
            "sourceType": "Azure Data Share"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles2/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Personal",
            "count": 7,
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "AB_Custom_Classifications",
            "classificationCategory": "Custom",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "count": 3,
            "path": "https://app.powerbi.com/groups/9bb0fb7a-79d3-43d9-826e-36f14811d467/datasets/",
            "sourceType": "Power BI"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 6,
            "sourceType": "Azure Cosmos DB"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 626
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 58,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Profisee MDM"
        },
        {
            "count": 6,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles3/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 4,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/rameshkalavarg/providers/Microsoft.Synapse/workspaces/fabrikamworkspace2/pipelines/Pipeline 1/activities/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "count": 2,
            "path": "https://fabrikamaribancosmosdb.documents.azure.com/dbs/SampleDB",
            "sourceType": "Azure Cosmos DB"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "Daily_ETL@derived_column:dest_c01",
            "sourceType": "demo_column_lineage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 1,
            "path": "https://synapsestorageadrm.core.windows.net/",
            "sourceType": "Azure Table Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 5,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.DATE_OF_BIRTH",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "TgtTable03#dest_c102_notransform",
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 4,
            "sourceType": "SQL Server"
        },
        {
            "count": 6,
            "sourceType": "Azure Cosmos DB"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.AGE",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.MEDICAL_ACCOUNT_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "https://fabrikamdwadls.core.windows.net/",
            "sourceType": "Azure Files"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 3,
            "sourceType": "Cassandra"
        },
        {
            "classificationCategory": "Custom",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Government",
            "count": 7,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 3,
            "sourceType": "demo_process"
        },
        {
            "classification": "MICROSOFT.PERSONAL.IPADDRESS",
            "classificationCategory": "Personal",
            "count": 2,
            "sourceType": "demo_column"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SourceTable03",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "https://jifeadlsgen2.core.windows.net/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "AB_Custom_Classifications",
            "classificationCategory": "Custom",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "Daily_ETL",
            "sourceType": "demo_process"
        },
        {
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 1,
            "path": "Daily_ETL@derived_column:dest_c02",
            "sourceType": "demo_column_lineage"
        },
        {
            "count": 1,
            "path": "https://fabrikamdwadls.core.windows.net/",
            "sourceType": "Azure Table Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.DATE_OF_BIRTH",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "count": 1,
            "path": "https://synapsestorageadrm.core.windows.net/",
            "sourceType": "Azure Files"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 1,
            "path": "https://fabrikamworkspace2.azuresynapse.net/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourcegroups/jife-rg/providers/Microsoft.DataShare/accounts/jifeDataShareAccountDept2/shareSubscriptions/",
            "sourceType": "Azure Data Share"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Custom",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "count": 129,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.IPADDRESS",
            "classificationCategory": "Personal",
            "count": 2,
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.core.windows.net/",
            "sourceType": "Azure Table Storage"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 6,
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SourceTable03#source_c05",
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 156,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "count": 1,
            "path": "Stored_Proc:Do_Something",
            "sourceType": "demo_process"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 121,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SrcTable03",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "SQL Server"
        },
        {
            "count": 8,
            "sourceType": "demo_column_lineage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 2,
            "path": "mssql://azdemosrv01.database.windows.net/AdventureWorksSimple",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 835
        },
        {
            "classificationCategory": "Financial",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 2,
            "sourceType": "aws"
        },
        {
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 41,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 36,
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 8,
            "sourceType": "demo_column_lineage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "count": 10,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-combo/2021/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Government",
            "count": 5,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "SourceTable02",
            "sourceType": "demo_table"
        },
        {
            "count": 8,
            "sourceType": "Azure Table Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 2,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "https://jifeadlsgen2.core.windows.net/",
            "sourceType": "Azure Files"
        },
        {
            "count": 1,
            "path": "mssql://10.33.0.4/MSSQLSERVER",
            "sourceType": "SQL Server"
        },
        {
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourcegroups/jife-rg/providers/Microsoft.DataShare/accounts/jifeDataShareAccountDept1/shares/",
            "sourceType": "Azure Data Share"
        },
        {
            "classificationCategory": "Security",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/",
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.AUSTRALIA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 7,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 10,
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.NATIONAL_IDENTIFICATION_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 6,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.TAX_IDENTIFICATION_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.DATE_OF_BIRTH",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "SourceTable01",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.SECURITY.COMMON_PASSWORDS",
            "classificationCategory": "Security",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Personal",
            "count": 3,
            "path": "mssql://azdemosrv01.database.windows.net/AdventureWorksSimple",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 15,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 7,
            "sourceType": "SQL Server"
        },
        {
            "count": 1,
            "path": "SrcTable03#Src_c05",
            "sourceType": "demo_column"
        },
        {
            "count": 3,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 2,
            "path": "s3://azure-demo-joe/",
            "sourceType": "aws"
        },
        {
            "count": 3,
            "sourceType": "demo_process"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 7,
            "path": "/subscriptions/e614e12f-bdd2-427b-a2be-83dcc7a60060/resourceGroups/AlCapone/providers/Microsoft.DataFactory/factories/fabrikamtestdf-nk",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.core.windows.net/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 7,
            "sourceType": "SQL Server"
        },
        {
            "count": 1,
            "path": "https://clientdemostorage.core.windows.net/",
            "sourceType": "Azure Files"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.SOCIAL_SECURITY_NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "count": 8,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "https://fabrikamaribancosmosdb.documents.azure.com/dbs/farikamcosmosdb",
            "sourceType": "Azure Cosmos DB"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 6,
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 157,
            "sourceType": "Profisee MDM"
        },
        {
            "count": 13,
            "path": "mssql://azdemosrv01.database.windows.net/AdventureWorksSimple",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 3,
            "sourceType": "Cassandra"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.NATIONAL_IDENTIFICATION_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles2/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 3,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 2,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 1,
            "path": "SrcTable02",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.IPADDRESS",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SrcTable03#Src_c05",
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Custom",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Personal",
            "count": 7,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "https://synapsestorageadrm.core.windows.net/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 5,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "count": 26,
            "sourceType": "demo_column"
        },
        {
            "count": 46,
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 7,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.IPADDRESS",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SourceTable03#source_c05",
            "sourceType": "demo_column"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.PERSONAL.AGE",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "DestTable02#dest_c04_express",
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ROMANIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.AGE",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 12,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 3,
            "sourceType": "aws"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.AUSTRALIA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "Weekly_ETL",
            "sourceType": "demo_process"
        },
        {
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.core.windows.net/",
            "sourceType": "Azure Files"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 57,
            "sourceType": "Power BI"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.TAX_IDENTIFICATION_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles2/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 3,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 8,
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.MEDICAL_ACCOUNT_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "https://jifeadlsgen2.core.windows.net/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 18,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.CANADA.BANK_ACCOUNT_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 2,
            "path": "postgresql://fabrikam-azdb-postgresql.postgres.database.azure.com/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "CovidCohort",
            "classificationCategory": "Custom",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 8,
            "sourceType": "hive"
        },
        {
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "Weekly_ETL@derived_column:dest_c03",
            "sourceType": "demo_column_lineage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 2,
            "path": "mssql://azdemosrv01.database.windows.net/AdventureWorksSimple",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/fact/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "pyapacheatlas://hivetable02/",
            "sourceType": "hive"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 24,
            "sourceType": "demo_column"
        },
        {
            "count": 1,
            "path": "mssql://ninjasql.database.windows.net/",
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "count": 3,
            "path": "https://app.powerbi.com/groups/9bb0fb7a-79d3-43d9-826e-36f14811d467/reports/",
            "sourceType": "Power BI"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 8,
            "sourceType": "hive"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ROMANIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Personal",
            "count": 3,
            "sourceType": "Profisee MDM"
        },
        {
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Profisee MDM"
        },
        {
            "count": 1,
            "path": "SrcTable03",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 2,
            "path": "mssql://workspace-demo-nf.sql.azuresynapse.net/SQLPOOL1/dim/",
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "count": 12,
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Custom",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Personal",
            "count": 3,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "count": 1,
            "path": "https://capstoragecxvu42lfoohr2.core.windows.net/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 4,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 5,
            "sourceType": "SQL Server Integration Services"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/fabrikampurviewdb",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 103,
            "sourceType": "Azure Database for MySQL"
        },
        {
            "classificationCategory": "Personal",
            "count": 7,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "count": 8,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 1,
            "path": "https://fabrikamaribancosmosdb.documents.azure.com",
            "sourceType": "Azure Cosmos DB"
        },
        {
            "classificationCategory": "Government",
            "count": 2,
            "path": "mssql://sales-db-srv.database.windows.net/sales-db",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "https://clientdemostorage.core.windows.net/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 2,
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "https://jifeadlsgen2.core.windows.net/",
            "sourceType": "Azure Table Storage"
        },
        {
            "classification": "AB_Custom_Classifications",
            "classificationCategory": "Custom",
            "count": 1,
            "path": "/subscriptions/1ffe3217-455e-4544-a33d-f855377de8ed/resourceGroups/factories/providers/Microsoft.DataFactory/factories/client-demo-factory",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.ARGENTINA.DNI_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 1,
            "path": "https://clientdemostorage.core.windows.net/",
            "sourceType": "Azure Table Storage"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 152,
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "classificationCategory": "Government",
            "count": 5,
            "sourceType": "SQL Server"
        },
        {
            "count": 6,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles4/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.PERSONAL.NAME",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://adventureworks-synapse-demo.database.windows.net/AdventureWorks-synapse-demo",
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 17,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.EU.NATIONAL_IDENTIFICATION_NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 17,
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 1,
            "path": "cassandra://10.5.0.4:9042/ariban/",
            "sourceType": "Cassandra"
        },
        {
            "count": 1,
            "path": "pyapacheatlas://demo_update_lineage_input/",
            "sourceType": "hive"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 1,
            "path": "s3://azure-demo-joe/financials/",
            "sourceType": "aws"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 1,
            "path": "DestTable01#dest_c02",
            "sourceType": "demo_column"
        },
        {
            "classification": "MICROSOFT.PERSONAL.IPADDRESS",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SourceTable03",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 5,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.PERSONAL.AGE",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.PERSONAL.EMAIL",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "adb-5930284167956506.6.azuredatabricks.net",
            "sourceType": "hive"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/raw/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 8,
            "sourceType": "Azure Files"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "count": 4,
            "path": "mssql://10.33.0.4/MSSQLSERVER/adventureworks2019",
            "sourceType": "SQL Server"
        },
        {
            "count": 1,
            "path": "mssql://fabrikampurviewsqlserver.database.windows.net/",
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "count": 8,
            "sourceType": "Azure SQL Data Warehouse"
        },
        {
            "count": 19,
            "path": "https://app.powerbi.com/groups/",
            "sourceType": "Power BI"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://synapsestorageadrm.dfs.core.windows.net/covid19/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 79,
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 8,
            "path": "https://fabrikamstoacct.dfs.core.windows.net/twittercorp-geo/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 79,
            "sourceType": "Power BI"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BRAZIL.NATIONAL_ID_CARD",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "postgresql://purviewdemoserver01.postgres.database.azure.com/purview/public/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 8,
            "sourceType": "Azure Table Storage"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "count": 1,
            "path": "postgresql://fabrikam-azdb-postgresql.postgres.database.azure.com/postgres/",
            "sourceType": "Azure Database for PostgreSQL"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 41,
            "sourceType": "Azure Blob Storage"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://workspacedemolakenf.dfs.core.windows.net/synapse-demo-nf/cleansed/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "CovidCohort",
            "classificationCategory": "Custom",
            "count": 1,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourcegroups/jife-rg/providers/Microsoft.DataShare/accounts/jifeDataShareAccountDept2/shareSubscriptions/ProductCatalog/snapshots/",
            "sourceType": "Azure Data Share"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.DRIVERS_LICENSE_NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BULGARIA.PASSPORT.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "classificationCategory": "Personal",
            "count": 1,
            "path": "mssql://testsqlserver-nk.database.windows.net/testsqldtabase-nk",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 20,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.STATE",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 6,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "count": 1,
            "path": "Daily_ETL@derived_column:dest_combo01",
            "sourceType": "demo_column_lineage"
        },
        {
            "count": 5,
            "path": "ssisdb://fabrikamsqlsrv1.database.windows.net/LoadFabrikamDW/LoadFabrikamDW/",
            "sourceType": "SQL Server Integration Services"
        },
        {
            "count": 101,
            "path": "mysql://fabrikam-azdb-mysql.mysql.database.azure.com/sys/",
            "sourceType": "Azure Database for MySQL"
        },
        {
            "classification": "MICROSOFT.PERSONAL.US.PHONE_NUMBER",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER",
            "classificationCategory": "Financial",
            "count": 1,
            "path": "https://fabrikamstoragepurview.dfs.core.windows.net/s3financials/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Financial",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "count": 33,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles6/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 7,
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure Synapse Analytics"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 8,
            "sourceType": "Azure Files"
        },
        {
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://profiseepurview.profisee.biz/profisee/",
            "sourceType": "Profisee MDM"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.TAX_FILE_NUMBER",
            "classificationCategory": "Government",
            "count": 3,
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.CITY_NAME",
            "classificationCategory": "Government",
            "count": 7,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.PERSONAL.AGE",
            "classificationCategory": "Personal",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/e8c16a8a-e4a9-4a0f-aa40-b6f91d579011/resourceGroups/purview-demo-fabrikam/providers/Microsoft.DataFactory/factories/adf-for-purview-demo-fabrikam",
            "sourceType": "Azure Data Factory"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.US.ZIP_CODE",
            "classificationCategory": "Government",
            "count": 5,
            "path": "mssql://10.33.0.4/MSSQLSERVER/AdventureWorks2019",
            "sourceType": "SQL Server"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.BELGIUM.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "count": 1,
            "path": "DestTable03",
            "sourceType": "demo_table"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRALIA.BUSINESS.NUMBER",
            "classificationCategory": "Government",
            "count": 2,
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.DRIVERS.LICENSE.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "mssql://fabrikamsqlsrv1.database.windows.net/fabrikamsqldw",
            "sourceType": "Azure SQL Database"
        },
        {
            "classification": "MICROSOFT.PERSONAL.IPADDRESS",
            "classificationCategory": "Personal",
            "count": 1,
            "path": "SrcTable03",
            "sourceType": "demo_table"
        },
        {
            "classification": "None",
            "classificationCategory": "None",
            "count": 103,
            "sourceType": "Azure Database for MySQL"
        },
        {
            "classificationCategory": "Financial",
            "count": 2,
            "path": "https://fabrikamdwadls.blob.core.windows.net/csvfiles/FabrikamDWData/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classification": "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
            "classificationCategory": "Government",
            "count": 1,
            "path": "https://clientdemostorage.dfs.core.windows.net/sample-data/",
            "sourceType": "Azure Data Lake Storage Gen2"
        },
        {
            "classificationCategory": "Government",
            "count": 2,
            "path": "https://capstoragecxvu42lfoohr2.blob.core.windows.net/capfiles/",
            "sourceType": "Azure Blob Storage"
        },
        {
            "classificationCategory": "Government",
            "count": 1,
            "path": "/subscriptions/8c2c7b23-848d-40fe-b817-690d79ad9dfd/resourceGroups/FabrikamPurviewDemoRG/providers/Microsoft.DataFactory/factories/FabrikamSSISADF",
            "sourceType": "Azure Data Factory"
        }
    ],
    "snapshotTime": "2021-11-23T13:24:03Z"
}
```
</p>
</details>
