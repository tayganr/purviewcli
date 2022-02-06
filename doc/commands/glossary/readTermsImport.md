# pv glossary readTermsImport
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readTermsImport

## Description
Get the status of an import CSV operation.

## Syntax
```
pv glossary readTermsImport --operationGuid=<val>
```

## Required Arguments
`--operationGuid` (string)  
The globally unique identifier for async operation/job.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Glossary > [Get Import Csv Operation Status](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-import-csv-operation-status)
```
GET https://{accountName}.purview.azure.com/catalog/api/glossary/terms/import/{operationGuid}
```

## Examples
Get the status of an import CSV operation.
```powershell
pv glossary readTermsImport --operationGuid "54c3e5d0-90b3-4249-851c-0e3c4dba33c1"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "createTime": "2022-02-06T22:19:48.949+0000",
    "error": {
        "errorCode": 0,
        "errorMessage": ""
    },
    "id": "54c3e5d0-90b3-4249-851c-0e3c4dba33c1",
    "lastUpdateTime": "2022-02-06T22:19:50.824+0000",
    "properties": {
        "importedTerms": "51",
        "totalTermsDetected": "51"
    },
    "status": "SUCCEED"
}
```
</p>
</details>