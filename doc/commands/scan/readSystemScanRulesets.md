# pv scan readSystemScanRulesets
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readSystemScanRulesets

## Description
List all system scan rulesets for an account.

## Syntax
```
pv scan readSystemScanRulesets
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > System Scan Rulesets > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/system-scan-rulesets/list-all)
```
GET https://{accountName}.purview.azure.com/scan/systemScanRulesets
```

## Examples
List all system scan rulesets.
```powershell
pv scan readSystemScanRulesets
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 20,
    "value": [
        {
            "id": "systemscanrulesets/AzureCosmosDb",
            "kind": "AzureCosmosDb",
            "name": "AzureCosmosDb",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:48.683992Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:48.683992Z",
                "temporaryResourceFilters": []
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AzureSynapseWorkspace",
            "kind": "AzureSynapseWorkspace",
            "name": "AzureSynapseSQL",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:47.409701Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:47.409701Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AdlsGen2",
            "kind": "AdlsGen2",
            "name": "AdlsGen2",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-09T18:06:33.0707225Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-09T18:06:33.0707225Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "CSV",
                        "JSON",
                        "PSV",
                        "SSV",
                        "TSV",
                        "GZ",
                        "TXT",
                        "XML",
                        "PARQUET",
                        "AVRO",
                        "ORC",
                        "Documents",
                        "DOC",
                        "DOCM",
                        "DOCX",
                        "DOT",
                        "ODP",
                        "ODS",
                        "ODT",
                        "PDF",
                        "POT",
                        "PPS",
                        "PPSX",
                        "PPT",
                        "PPTM",
                        "PPTX",
                        "XLC",
                        "XLS",
                        "XLSB",
                        "XLSM",
                        "XLSX",
                        "XLT"
                    ]
                },
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 5
        },
        {
            "id": "systemscanrulesets/AmazonSql",
            "kind": "AmazonSql",
            "name": "AmazonSql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:48.4505692Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:48.4505692Z",
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AmazonS3",
            "kind": "AmazonS3",
            "name": "AmazonS3",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:48.2170936Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:48.2170936Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "CSV",
                        "JSON",
                        "PSV",
                        "SSV",
                        "TSV",
                        "GZ",
                        "TXT",
                        "XML",
                        "PARQUET",
                        "AVRO",
                        "ORC",
                        "Documents",
                        "DOC",
                        "DOCM",
                        "DOCX",
                        "DOT",
                        "ODP",
                        "ODS",
                        "ODT",
                        "PDF",
                        "POT",
                        "PPS",
                        "PPSX",
                        "PPT",
                        "PPTM",
                        "PPTX",
                        "XLC",
                        "XLS",
                        "XLSB",
                        "XLSM",
                        "XLSX",
                        "XLT"
                    ]
                },
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 4
        },
        {
            "id": "systemscanrulesets/AzureStorage",
            "kind": "AzureStorage",
            "name": "AzureStorage",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-09T18:06:32.2452994Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-09T18:06:32.2452994Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "CSV",
                        "JSON",
                        "PSV",
                        "SSV",
                        "TSV",
                        "GZ",
                        "TXT",
                        "XML",
                        "PARQUET",
                        "AVRO",
                        "ORC",
                        "Documents",
                        "DOC",
                        "DOCM",
                        "DOCX",
                        "DOT",
                        "ODP",
                        "ODS",
                        "ODT",
                        "PDF",
                        "POT",
                        "PPS",
                        "PPSX",
                        "PPT",
                        "PPTM",
                        "PPTX",
                        "XLC",
                        "XLS",
                        "XLSB",
                        "XLSM",
                        "XLSX",
                        "XLT"
                    ]
                },
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 5
        },
        {
            "id": "systemscanrulesets/AzureFileService",
            "kind": "AzureFileService",
            "name": "AzureFileService",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-09T18:06:32.5979674Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-09T18:06:32.5979674Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "CSV",
                        "JSON",
                        "PSV",
                        "SSV",
                        "TSV",
                        "GZ",
                        "TXT",
                        "XML",
                        "PARQUET",
                        "AVRO",
                        "ORC",
                        "Documents",
                        "DOC",
                        "DOCM",
                        "DOCX",
                        "DOT",
                        "ODP",
                        "ODS",
                        "ODT",
                        "PDF",
                        "POT",
                        "PPS",
                        "PPSX",
                        "PPT",
                        "PPTM",
                        "PPTX",
                        "XLC",
                        "XLS",
                        "XLSB",
                        "XLSM",
                        "XLSX",
                        "XLT"
                    ]
                },
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 5
        },
        {
            "id": "systemscanrulesets/AzureSynapseServerlessSql",
            "kind": "AzureSynapseServerlessSql",
            "name": "AzureSynapseSQL",
            "properties": {
                "collection": null,
                "createdAt": "2020-12-02T00:55:25.5613448Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2020-12-02T00:55:25.5613448Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 1
        },
        {
            "id": "systemscanrulesets/AzurePostgreSql",
            "kind": "AzurePostgreSql",
            "name": "AzurePostgreSql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:50.0934633Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:50.0934633Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/Teradata",
            "kind": "Teradata",
            "name": "Teradata",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:51.5271554Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:51.5271554Z",
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 2
        },
        {
            "id": "systemscanrulesets/AzureSynapseDedicatedSql",
            "kind": "AzureSynapseDedicatedSql",
            "name": "AzureSynapseSQL",
            "properties": {
                "collection": null,
                "createdAt": "2020-12-02T00:55:25.2847266Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2020-12-02T00:55:25.2847266Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 1
        },
        {
            "id": "systemscanrulesets/AzureDataExplorer",
            "kind": "AzureDataExplorer",
            "name": "AzureDataExplorer",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:48.9180315Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:48.9180315Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AmazonPostgreSql",
            "kind": "AmazonPostgreSql",
            "name": "AmazonPostgreSql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:49.6290897Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:49.6290897Z",
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/SqlServerDatabase",
            "kind": "SqlServerDatabase",
            "name": "SqlServer",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:50.3344463Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:50.3344463Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AzureSqlDatabase",
            "kind": "AzureSqlDatabase",
            "name": "AzureSqlDatabase",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:49.3857041Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:49.3857041Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AzureMySql",
            "kind": "AzureMySql",
            "name": "AzureMySql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:51.026444Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:51.026444Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AzureSqlDatabaseManagedInstance",
            "kind": "AzureSqlDatabaseManagedInstance",
            "name": "AzureSqlDatabaseManagedInstance",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:50.5650044Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:50.5650044Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AdlsGen1",
            "kind": "AdlsGen1",
            "name": "AdlsGen1",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-09T18:06:32.8353486Z",
                "description": "Microsoft default scan rule set that includes all supported file types for schema extraction and classification, and all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-09T18:06:32.8353486Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "CSV",
                        "JSON",
                        "PSV",
                        "SSV",
                        "TSV",
                        "GZ",
                        "TXT",
                        "XML",
                        "PARQUET",
                        "AVRO",
                        "ORC",
                        "Documents",
                        "DOC",
                        "DOCM",
                        "DOCX",
                        "DOT",
                        "ODP",
                        "ODS",
                        "ODT",
                        "PDF",
                        "POT",
                        "PPS",
                        "PPSX",
                        "PPT",
                        "PPTM",
                        "PPTX",
                        "XLC",
                        "XLS",
                        "XLSB",
                        "XLSM",
                        "XLSX",
                        "XLT"
                    ]
                },
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 5
        },
        {
            "id": "systemscanrulesets/AzureSqlDataWarehouse",
            "kind": "AzureSqlDataWarehouse",
            "name": "AzureSqlDataWarehouse",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:50.7966194Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:50.7966194Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        },
        {
            "id": "systemscanrulesets/AmazonMySql",
            "kind": "AmazonMySql",
            "name": "AmazonMySql",
            "properties": {
                "collection": null,
                "createdAt": "2021-12-02T09:24:49.8617837Z",
                "description": "Microsoft default scan rule set that includes all supported system classification rules",
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2021-12-02T09:24:49.8617837Z",
                "temporaryResourceFilters": null
            },
            "scanRulesetType": "System",
            "status": "Enabled",
            "version": 3
        }
    ]
}
```
</p>
</details>