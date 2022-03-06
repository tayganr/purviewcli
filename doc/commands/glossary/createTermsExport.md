# pv glossary createTermsExport
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > createTermsExport

## Description
Export glossary terms to a csv file.

## Syntax
```
pv glossary createTermsExport --glossaryGuid=<val> --termGuid=<val>... [--includeTermHierarchy]
```

## Required Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

`--termGuid` (string)  
The globally unique identifier for glossary term.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy [default: false].

## API Mapping
Catalog Data Plane > Glossary > [Export Glossary Terms As Csv](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/export-glossary-terms-as-csv)
```
POST https://{accountName}.purview.azure.com/catalog/api/glossary/{glossaryGuid}/terms/export
```

## Examples
Export glossary terms to a CSV file.
```powershell
pv glossary createTermsExport --glossaryGuid "125e2575-5823-4887-89f0-ff03a70f7c3a" --termGuid "4ba01c1e-5ef8-4457-87b4-37e2054b1cb9" --termGuid "9d1dec92-fb42-49ea-8fb8-5a0ff8898a64" --termGuid "8f925987-62d1-4ca7-a90b-3861162651e9"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "export": "/YOUR_FOLDER_PATH/export.csv",
    "status_code": 200
}
```
</p>
</details>