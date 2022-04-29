# pv entity importBusinessMetadata
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > importBusinessMetadata

## Description
Import business metadata in bulk from a CSV file.

## Syntax
```
pv entity importBusinessMetadata --bmFile=<val>
```

## Required Arguments
`--bmFile` (string)  
File path to a valid business metadata template CSV file.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Import Business Attributes](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/import-business-attributes)
```
POST https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/businessmetadata/import
```

## Examples
Import business metadata in bulk from a CSV file.
```powershell
pv entity importBusinessMetadata --bmFile "/path/to/template.csv"
```
<details><summary>Example CSV.</summary>
<p>

```csv
EntityType,EntityUniqueAttributeValue,BusinessAttributeName,BusinessAttributeValue,EntityUniqueAttributeName[optional]
azure_datalake_gen2_path,https://STORAGE_ACCOUNT.dfs.core.windows.net/bing/data/merged.parquet,myBizMetadata1.bizAttr1,hello,
```
</p>
</details>