# pv types readEntityDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readEntityDef

## Description
Get the Entity definition for the given GUID or by its name (unique).

## Syntax
```
pv types readEntityDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the guid.

`--name` (string)  
The name of the entity.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Entity Definition By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-entity-definition-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/entitydef/guid/{guid}
```

Catalog Data Plane > Types > [Get Entity Definition By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-entity-definition-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/entitydef/name/{name}
```

## Examples
Get an entity definition by name.
```powershell
pv types readEntityDef --name "azure_sql_table"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "attributeDefs": [
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isOptional": true,
            "isUnique": false,
            "name": "principalId",
            "typeName": "int",
            "valuesMaxCount": 1,
            "valuesMinCount": 0
        },
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isOptional": true,
            "isUnique": false,
            "name": "objectType",
            "typeName": "string",
            "valuesMaxCount": 1,
            "valuesMinCount": 0
        },
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isOptional": true,
            "isUnique": false,
            "name": "createTime",
            "typeName": "date",
            "valuesMaxCount": 1,
            "valuesMinCount": 0
        },
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isOptional": true,
            "isUnique": false,
            "name": "modifiedTime",
            "typeName": "date",
            "valuesMaxCount": 1,
            "valuesMinCount": 0
        }
    ],
    "category": "ENTITY",
    "createTime": 1616124550225,
    "createdBy": "admin",
    "description": "azure_sql_table",
    "guid": "7d92a449-f7e8-812f-5fc8-ca6127ba90bd",
    "lastModifiedTS": "1",
    "name": "azure_sql_table",
    "options": {
        "purviewEntityExtDef": "{}",
        "schemaElementsAttribute": "columns"
    },
    "relationshipAttributeDefs": [
        {
            "cardinality": "SET",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "schema",
            "relationshipTypeName": "avro_schema_associatedEntities",
            "typeName": "array<avro_schema>",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SET",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "inputToProcesses",
            "relationshipTypeName": "dataset_process_inputs",
            "typeName": "array<Process>",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": false,
            "isUnique": false,
            "name": "dbSchema",
            "relationshipTypeName": "azure_sql_schema_tables",
            "typeName": "azure_sql_schema",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SET",
            "constraints": [
                {
                    "type": "ownedRef"
                }
            ],
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "columns",
            "relationshipTypeName": "azure_sql_table_columns",
            "typeName": "array<azure_sql_column>",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SET",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "attachedSchema",
            "relationshipTypeName": "dataset_attached_schemas",
            "typeName": "array<schema>",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SET",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "meanings",
            "relationshipTypeName": "AtlasGlossarySemanticAssignment",
            "typeName": "array<AtlasGlossaryTerm>",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SET",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "outputFromProcesses",
            "relationshipTypeName": "process_dataset_outputs",
            "typeName": "array<Process>",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        },
        {
            "cardinality": "SINGLE",
            "includeInNotification": false,
            "isIndexable": false,
            "isLegacyAttribute": false,
            "isOptional": true,
            "isUnique": false,
            "name": "tabular_schema",
            "relationshipTypeName": "tabular_schema_datasets",
            "typeName": "tabular_schema",
            "valuesMaxCount": -1,
            "valuesMinCount": -1
        }
    ],
    "serviceType": "Azure SQL Database",
    "subTypes": [],
    "superTypes": [
        "DataSet"
    ],
    "typeVersion": "1.0",
    "updateTime": 1616124550225,
    "updatedBy": "admin",
    "version": 1
}
```
</p>
</details>

Get an entity definition by guid.
```powershell
pv types readEntityDef --guid "7d92a449-f7e8-812f-5fc8-ca6127ba90bd"
```