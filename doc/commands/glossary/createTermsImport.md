# pv glossary createTermsImport
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTermsImport

## Description
Import glossary terms from local csv file.

## Syntax
```
pv glossary createTermsImport --glossaryFile=<val> [--glossaryGuid=<val> --includeTermHierarchy]
```

## Required Arguments
`--glossaryFile` (string)  
File path to a valid JSON document.

## Optional Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy.

## API Mapping
Catalog Data Plane > Glossary > [Import Glossary Terms Via Csv](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/import-glossary-terms-via-csv)
```
POST https://{accountName}.purview.azure.com/catalog/api/glossary/{glossaryGuid}/terms/import
```

Catalog Data Plane > Glossary > [Import Glossary Terms from local csv file by glossaryName](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/import-glossary-terms-via-csv-by-glossary-name)
```
POST https://{accountName}.purview.azure.com/catalog/api/glossary/name/{glossaryName}/terms/import
```

## Examples
Upload glossary terms via a CSV file.
```powershell
pv glossary createTermsImport --glossaryGuid "125e2575-5823-4887-89f0-ff03a70f7c3a" --glossaryFile "/path/to/file.json"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "createTime": "2022-02-26T12:13:31.065+0000",
    "error": {
        "errorCode": 0,
        "errorMessage": ""
    },
    "id": "60c8f03b-53f9-402d-bb7d-aa03871759ba",
    "lastUpdateTime": "2022-02-26T12:13:31.065+0000",
    "properties": {
        "importedTerms": "0",
        "totalTermsDetected": "-1"
    },
    "status": "Running"
}
```
</p>
</details>