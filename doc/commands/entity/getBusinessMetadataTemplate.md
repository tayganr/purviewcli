# pv entity getBusinessMetadataTemplate
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > getBusinessMetadataTemplate

## Description
Get a sample template for uploading/creating business metadata in bulk.

## Syntax
```
pv entity getBusinessMetadataTemplate
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Sample Business Metadata Template](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-sample-business-metadata-template)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/businessmetadata/import/template
```

## Examples
Download a sample template for uploading/creating business metadata in bulk.
```powershell
pv entity getBusinessMetadataTemplate
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "export": "/YOUR_CURRENT_DIRECTORY/export.csv",
    "status_code": 200
}
```
</p>
</details>