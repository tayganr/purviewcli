# pv scan readScanRulesets
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScanRulesets

## Description
List scan rulesets in Data catalog

## Syntax
```
pv scan readScanRulesets
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Rulesets > [List All](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-rulesets/list-all)
```
GET https://{accountName}.purview.azure.com/scan/scanrulesets
```

## Examples
List all custom scan rulesets.
```powershell
pv scan readScanRulesets
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "value": [
        {
            "id": "scanrulesets/adls_parquet_only",
            "kind": "AdlsGen2",
            "name": "adls_parquet_only",
            "properties": {
                "collection": null,
                "createdAt": "2022-02-27T21:22:19.0970457Z",
                "description": null,
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [],
                "lastModifiedAt": "2022-02-27T21:22:19.0970462Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "PARQUET"
                    ]
                },
                "temporaryResourceFilters": [
                    {
                        "ingestTemporaryResource": true,
                        "resourceFilterPattern": "(_SUCCESS|_started_\\d*|_committed_\\d*|_committed_vacuum\\d*)$"
                    }
                ]
            },
            "scanRulesetType": "Custom",
            "status": "Enabled",
            "version": 1
        },
        {
            "id": "scanrulesets/adls_include_custom_classification",
            "kind": "AdlsGen2",
            "name": "adls_include_custom_classification",
            "properties": {
                "collection": null,
                "createdAt": "2022-02-27T21:22:45.1800309Z",
                "description": null,
                "excludedSystemClassifications": [],
                "includedCustomClassificationRuleNames": [
                    "twitter_handle"
                ],
                "lastModifiedAt": "2022-02-27T21:22:45.1800313Z",
                "scanningRule": {
                    "customFileExtensions": null,
                    "fileExtensions": [
                        "CSV",
                        "JSON",
                        "PSV",
                        "SSV",
                        "TSV",
                        "TXT",
                        "XML",
                        "PARQUET",
                        "AVRO",
                        "ORC",
                        "Documents",
                        "GZ",
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
            "scanRulesetType": "Custom",
            "status": "Enabled",
            "version": 1
        }
    ]
}
```
</p>
</details>