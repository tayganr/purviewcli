# pv types readStatistics
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readStatistics

## Description
Get a count of entities by type.

## Syntax
```
pv types readStatistics
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/statistics
```

## Examples
Get a count of entities by type.
```powershell
pv types readStatistics
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "typeStatistics": {
        "AtlasGlossary": {
            "count": 1
        },
        "AtlasGlossaryTerm": {
            "count": 51
        },
        "adf_copy_activity": {
            "count": 2
        },
        "adf_pipeline": {
            "count": 2
        },
        "azure_data_factory": {
            "count": 1
        },
        "azure_datalake_gen2_filesystem": {
            "count": 1
        },
        "azure_datalake_gen2_path": {
            "count": 6
        },
        "azure_datalake_gen2_resource_set": {
            "count": 2
        },
        "azure_datalake_gen2_service": {
            "count": 1
        },
        "azure_sql_db": {
            "count": 1
        },
        "azure_sql_schema": {
            "count": 2
        },
        "azure_sql_server": {
            "count": 1
        },
        "azure_sql_table": {
            "count": 12
        },
        "azure_sql_view": {
            "count": 3
        },
        "azure_storage_account": {
            "count": 1
        }
    }
}
```
</p>
</details>
