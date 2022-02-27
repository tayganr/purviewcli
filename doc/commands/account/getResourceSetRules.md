# pv account getResourceSetRules
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getResourceSetRules

## Description
List all resource sets.

## Syntax
```
pv account getResourceSetRules
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Resource Set Rules > [List Resource Set Rules](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/resource-set-rules/list-resource-set-rules)
```
GET https://{accountName}.purview.azure.com/account/resourceSetRuleConfigs
```

## Examples
List all resource sets.
```powershell
pv account getResourceSetRules
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 1,
    "value": [
        {
            "advancedResourceSet": {
                "modifiedAt": "2022-02-23T09:48:50.3471638Z",
                "resourceSetProcessing": "Default"
            },
            "name": "defaultResourceSetRuleConfig",
            "pathPatternConfig": {
                "acceptedPatterns": [],
                "complexReplacers": [
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": true,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "SparkPath",
                        "typeName": "Microsoft.DataMap.PathPattern.SparkPathReplacer"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": true,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "Date(yyyy/mm/dd)InPath",
                        "typeName": "Microsoft.DataMap.PathPattern.DatePatternPathReplacer"
                    }
                ],
                "createdBy": "AzureDataCatalog",
                "enableDefaultPatterns": true,
                "lastUpdatedTimestamp": 1645609730,
                "modifiedBy": "AzureDataCatalog",
                "normalizationRules": [
                    {
                        "description": "Trim leading and trailing spaces for all parts of the qualified name",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_storage_account",
                            "azure_blob_service",
                            "azure_blob_container",
                            "azure_blob_path",
                            "azure_sql_server",
                            "azure_sql_db",
                            "azure_sql_schema",
                            "azure_sql_table",
                            "azure_sql_column",
                            "azure_datalake_gen1_account",
                            "azure_datalake_gen1_path",
                            "azure_datalake_gen2_service",
                            "azure_datalake_gen2_filesystem",
                            "azure_datalake_gen2_path",
                            "azure_data_factory",
                            "adf_pipeline",
                            "adf_dataflow_activity",
                            "adf_copy_activity",
                            "adf_executeSsisPackage_activity",
                            "adf_dataflow_activity_run",
                            "adf_copy_activity_run",
                            "adf_executeSsisPackage_activity_run",
                            "adf_activity_operation",
                            "adf_dataflow_operation",
                            "adf_copy_operation",
                            "adf_executeSsisPackage_operation",
                            "azure_cosmosdb_account",
                            "azure_cosmosdb_database",
                            "azure_cosmosdb_sqlapi_collection",
                            "azure_file_service",
                            "azure_file_share",
                            "azure_file_directory",
                            "azure_file",
                            "azure_sql_dw",
                            "azure_sql_dw_schema",
                            "azure_sql_dw_table",
                            "azure_sql_dw_column",
                            "azure_sql_mi",
                            "azure_sql_mi_db",
                            "azure_sql_mi_schema",
                            "azure_sql_mi_table",
                            "azure_sql_mi_column",
                            "azure_cognitive_search_service",
                            "azure_cognitive_search_index",
                            "azure_data_explorer_cluster",
                            "azure_data_explorer_database",
                            "azure_data_explorer_table",
                            "azure_data_explorer_column",
                            "ads_account",
                            "ads_share",
                            "ads_share_subscription",
                            "ads_org_dataset",
                            "ads_sent_snapshot",
                            "aws_s3_v2_bucket",
                            "aws_s3_v2_directory",
                            "aws_s3_v2_object"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Trim Section Spaces",
                        "regex": {
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(^\\s+)|(\\s+[/:.]\\s+)|([/:.]\\s+)|(\\s+[/:.])|(\\s+$)"
                        },
                        "replaceWith": "TrimSpaces",
                        "version": 1.0
                    },
                    {
                        "description": "Remove all spaces from the hostname",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_storage_account",
                            "azure_blob_service",
                            "azure_blob_container",
                            "azure_blob_path",
                            "azure_sql_server",
                            "azure_sql_db",
                            "azure_sql_schema",
                            "azure_sql_table",
                            "azure_sql_column",
                            "azure_datalake_gen1_account",
                            "azure_datalake_gen1_path",
                            "azure_datalake_gen2_service",
                            "azure_datalake_gen2_filesystem",
                            "azure_datalake_gen2_path",
                            "azure_cosmosdb_account",
                            "azure_cosmosdb_database",
                            "azure_cosmosdb_sqlapi_collection",
                            "azure_file_service",
                            "azure_file_share",
                            "azure_file_directory",
                            "azure_file",
                            "azure_sql_dw",
                            "azure_sql_dw_schema",
                            "azure_sql_dw_table",
                            "azure_sql_dw_column",
                            "azure_sql_mi",
                            "azure_sql_mi_db",
                            "azure_sql_mi_schema",
                            "azure_sql_mi_table",
                            "azure_sql_mi_column",
                            "azure_cognitive_search_service",
                            "azure_cognitive_search_index",
                            "azure_data_explorer_cluster",
                            "azure_data_explorer_database",
                            "azure_data_explorer_table",
                            "azure_data_explorer_column",
                            "ads_account",
                            "ads_share",
                            "ads_share_subscription",
                            "ads_org_dataset",
                            "ads_sent_snapshot",
                            "aws_s3_v2_bucket",
                            "aws_s3_v2_directory",
                            "aws_s3_v2_object"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Remove Hostname Spaces",
                        "regex": {
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(://|urn:).*?\\s*.*?(:|/)"
                        },
                        "replaceWith": "RemoveHostnameSpaces",
                        "version": 1.0
                    },
                    {
                        "description": "Remove square brackets from the path and encode the space between the square brackets.",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_sql_db",
                            "azure_sql_schema",
                            "azure_sql_table",
                            "azure_sql_column",
                            "azure_sql_dw",
                            "azure_sql_dw_schema",
                            "azure_sql_dw_table",
                            "azure_sql_dw_column",
                            "azure_sql_mi",
                            "azure_sql_mi_db",
                            "azure_sql_mi_schema",
                            "azure_sql_mi_table",
                            "azure_sql_mi_column"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Remove Square Brackets",
                        "regex": {
                            "minLetters": 3,
                            "options": 8,
                            "regexStr": "\\[[^/]*?\\]"
                        },
                        "replaceWith": "RemoveBracketsAndEncodeSpaces",
                        "version": 1.0
                    },
                    {
                        "description": "Lowercase the file extension, if present.",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_blob_path",
                            "azure_datalake_gen1_path",
                            "azure_datalake_gen2_path",
                            "azure_file",
                            "aws_s3_v2_object"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Lowercase File Extension",
                        "regex": {
                            "minLetters": 3,
                            "options": 8,
                            "regexStr": "\\.[^\\.]{2,5}$"
                        },
                        "replaceWith": "ToLowerCase",
                        "version": 1.0
                    },
                    {
                        "description": "Lower case the hostname",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_storage_account",
                            "azure_blob_service",
                            "azure_blob_container",
                            "azure_blob_path",
                            "azure_sql_server",
                            "azure_sql_db",
                            "azure_sql_schema",
                            "azure_sql_table",
                            "azure_sql_column",
                            "azure_datalake_gen1_account",
                            "azure_datalake_gen1_path",
                            "azure_datalake_gen2_service",
                            "azure_datalake_gen2_filesystem",
                            "azure_datalake_gen2_path",
                            "azure_cosmosdb_account",
                            "azure_cosmosdb_database",
                            "azure_cosmosdb_sqlapi_collection",
                            "azure_file_service",
                            "azure_file_share",
                            "azure_file_directory",
                            "azure_file",
                            "azure_sql_dw",
                            "azure_sql_dw_schema",
                            "azure_sql_dw_table",
                            "azure_sql_dw_column",
                            "azure_sql_mi",
                            "azure_sql_mi_db",
                            "azure_sql_mi_schema",
                            "azure_sql_mi_table",
                            "azure_sql_mi_column",
                            "azure_cognitive_search_service",
                            "azure_cognitive_search_index",
                            "azure_data_explorer_cluster",
                            "azure_data_explorer_database",
                            "azure_data_explorer_table",
                            "azure_data_explorer_column",
                            "aws_s3_v2_bucket",
                            "aws_s3_v2_directory",
                            "aws_s3_v2_object"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Lowercase hostname",
                        "regex": {
                            "minLetters": 3,
                            "options": 8,
                            "regexStr": "(://|urn:).*?(:|/)"
                        },
                        "replaceWith": "ToLowerCase",
                        "version": 1.0
                    },
                    {
                        "description": "Lower case the scheme (http, https, s3, etc)",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_storage_account",
                            "azure_blob_service",
                            "azure_blob_container",
                            "azure_blob_path",
                            "azure_sql_server",
                            "azure_sql_db",
                            "azure_sql_schema",
                            "azure_sql_table",
                            "azure_sql_column",
                            "azure_datalake_gen1_account",
                            "azure_datalake_gen1_path",
                            "azure_datalake_gen2_service",
                            "azure_datalake_gen2_filesystem",
                            "azure_datalake_gen2_path",
                            "azure_cosmosdb_account",
                            "azure_cosmosdb_database",
                            "azure_cosmosdb_sqlapi_collection",
                            "azure_file_service",
                            "azure_file_share",
                            "azure_file_directory",
                            "azure_file",
                            "azure_sql_dw",
                            "azure_sql_dw_schema",
                            "azure_sql_dw_table",
                            "azure_sql_dw_column",
                            "azure_sql_mi",
                            "azure_sql_mi_db",
                            "azure_sql_mi_schema",
                            "azure_sql_mi_table",
                            "azure_sql_mi_column",
                            "azure_cognitive_search_service",
                            "azure_cognitive_search_index",
                            "azure_data_explorer_cluster",
                            "azure_data_explorer_database",
                            "azure_data_explorer_table",
                            "azure_data_explorer_column",
                            "aws_s3_v2_bucket",
                            "aws_s3_v2_directory",
                            "aws_s3_v2_object"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Lowercase scheme",
                        "regex": {
                            "minLetters": 2,
                            "options": 8,
                            "regexStr": "^[^:]+:"
                        },
                        "replaceWith": "ToLowerCase",
                        "version": 1.0
                    },
                    {
                        "description": "Removes double slashes that are not following a colon",
                        "disabled": false,
                        "dynamicReplacement": false,
                        "entityTypes": [
                            "azure_storage_account",
                            "azure_blob_service",
                            "azure_blob_container",
                            "azure_blob_path",
                            "azure_sql_server",
                            "azure_sql_db",
                            "azure_sql_schema",
                            "azure_sql_table",
                            "azure_sql_column",
                            "azure_datalake_gen1_account",
                            "azure_datalake_gen1_path",
                            "azure_datalake_gen2_service",
                            "azure_datalake_gen2_filesystem",
                            "azure_datalake_gen2_path",
                            "azure_data_factory",
                            "adf_pipeline",
                            "adf_dataflow_activity",
                            "adf_copy_activity",
                            "adf_executeSsisPackage_activity",
                            "adf_dataflow_activity_run",
                            "adf_copy_activity_run",
                            "adf_executeSsisPackage_activity_run",
                            "adf_activity_operation",
                            "adf_dataflow_operation",
                            "adf_copy_operation",
                            "adf_executeSsisPackage_operation",
                            "azure_cosmosdb_account",
                            "azure_cosmosdb_database",
                            "azure_cosmosdb_sqlapi_collection",
                            "azure_file_service",
                            "azure_file_share",
                            "azure_file_directory",
                            "azure_file",
                            "azure_sql_dw",
                            "azure_sql_dw_schema",
                            "azure_sql_dw_table",
                            "azure_sql_dw_column",
                            "azure_sql_mi",
                            "azure_sql_mi_db",
                            "azure_sql_mi_schema",
                            "azure_sql_mi_table",
                            "azure_sql_mi_column",
                            "azure_cognitive_search_service",
                            "azure_cognitive_search_index",
                            "azure_data_explorer_cluster",
                            "azure_data_explorer_database",
                            "azure_data_explorer_table",
                            "azure_data_explorer_column",
                            "ads_account",
                            "ads_share",
                            "ads_share_subscription",
                            "ads_org_dataset",
                            "ads_sent_snapshot",
                            "aws_s3_v2_bucket",
                            "aws_s3_v2_directory",
                            "aws_s3_v2_object"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Remove double slash",
                        "regex": {
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(?<=[^:])/{2,}"
                        },
                        "replaceWith": "/",
                        "version": 1.0
                    },
                    {
                        "description": "Lowercases the subscription name, resource group name, provider name, factory name, pipeline name, and activity name.",
                        "disabled": false,
                        "dynamicReplacement": true,
                        "entityTypes": [
                            "azure_data_factory",
                            "adf_pipeline",
                            "adf_dataflow_activity",
                            "adf_copy_activity",
                            "adf_executeSsisPackage_activity",
                            "adf_dataflow_activity_run",
                            "adf_copy_activity_run",
                            "adf_executeSsisPackage_activity_run",
                            "adf_activity_operation",
                            "adf_dataflow_operation",
                            "adf_copy_operation",
                            "adf_executeSsisPackage_operation"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Lower case ADF Data",
                        "regex": {
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "((?<=/subscriptions/)[^/]+)|((?<=/resourceGroups/)[^/]+)|((?<=/providers/)[^/]+)|((?<=/factories/)[^/]+)|((?<=/pipelines/)[^/]+)|((?<=/activities/)[^/]+)"
                        },
                        "replaceWith": "ToLowerCase",
                        "version": 2.0
                    },
                    {
                        "description": "If an ADLSGen1 asset is using http or https, convert the scheme to adl://.",
                        "disabled": false,
                        "dynamicReplacement": false,
                        "entityTypes": [
                            "azure_datalake_gen1_account",
                            "azure_datalake_gen1_path"
                        ],
                        "lastUpdatedTimestamp": 1598029957,
                        "name": "Convert ADLSGen1 to adl scheme",
                        "regex": {
                            "minLetters": 4,
                            "options": 8,
                            "regexStr": "http(s)*://"
                        },
                        "replaceWith": "adl://",
                        "version": 1.0
                    }
                ],
                "regexReplacers": [
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "Guid",
                        "regex": {
                            "minHex": 32,
                            "options": 9,
                            "regexStr": "([0-9A-F]{32}|[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})"
                        },
                        "replaceWith": "{GUID}"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": true,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "Number",
                        "regex": {
                            "minDigits": 1,
                            "options": 8,
                            "regexStr": "^\\d+$"
                        },
                        "replaceWith": "{N}"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "yyyy-mm-ddThh-MM-ss",
                        "regex": {
                            "minDigits": 14,
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(20)[1-9][0-9]([-\\._@]?)(0[1-9]|1[012])([-\\._@]?)(0[1-9]|[12][0-9]|3[01])([T])(2[0-3]|[01]?[0-9])([-\\._@]?)([0-5][0-9])([-\\._@]?)([0-5][0-9])(Z)?"
                        },
                        "replaceWith": "{Year}$2{Month}$4{Day}$6{Hour}$8{Minute}$10{Second}$12"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "yyyy-mm-ddThh",
                        "regex": {
                            "minDigits": 10,
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(20)[1-9][0-9]([-\\._@]?)(0[1-9]|1[012])([-\\._@]?)(0[1-9]|[12][0-9]|3[01])([T])(2[0-3]|[01]?[0-9])(Z)?"
                        },
                        "replaceWith": "{Year}$2{Month}$4{Day}$6{Hour}$8"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "yyyy-mm-ddZ",
                        "regex": {
                            "minDigits": 8,
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(20)[1-9][0-9]([-\\._@]?)(0[1-9]|1[012])([-\\._@]?)(0[1-9]|[12][0-9]|3[01])(Z)"
                        },
                        "replaceWith": "{Year}$2{Month}$4{Day}$6"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "yyyy-mm-dd-hhZ",
                        "regex": {
                            "minDigits": 10,
                            "minLetters": 1,
                            "options": 8,
                            "regexStr": "(20)[1-9][0-9]([-\\._@]?)(0[1-9]|1[012])([-\\._@]?)(0[1-9]|[12][0-9]|3[01])([-\\._@]?)(2[0-3]|[01]?[0-9])(Z)"
                        },
                        "replaceWith": "{Year}$2{Month}$4{Day}$6{Hour}$8"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "yyyy-mm-dd",
                        "regex": {
                            "minDigits": 8,
                            "options": 8,
                            "regexStr": "([-\\.=_@]|^)(20)[1-9][0-9]([-\\._@])(0[1-9]|1[012])([-\\._@])(0[1-9]|[12][0-9]|3[01])([-\\.=_@]|$)"
                        },
                        "replaceWith": "$1{Year}$3{Month}$5{Day}$7"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "doNotReplaceRegex": {
                            "minDigits": 1,
                            "minLetters": 1,
                            "options": 9,
                            "regexStr": "(?<=[-\\.=_@]|^)[v](\\d+)[\\.](\\d+)[\\.]?(\\d+)?(?=[-\\.=_@]|$)"
                        },
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "NumberBetweenDelimiter",
                        "regex": {
                            "minDigits": 1,
                            "options": 8,
                            "regexStr": "(?<=[-\\.=_@]|^)([\\d]+)(?=[-\\.=_@]|$)"
                        },
                        "replaceWith": "{N}"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "doNotReplaceRegex": {
                            "minLetters": 3,
                            "options": 9,
                            "regexStr": "([-\\._@]|^)[v](\\d+)[\\.](\\d+)[\\.]?(\\d+)?([-\\._@]|$)"
                        },
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "4ByteHex",
                        "regex": {
                            "minHex": 8,
                            "options": 9,
                            "regexStr": "(?<=[-\\._@]|^)([0-9A-F]{8,16})(?=[-\\._@]|$)"
                        },
                        "replaceWith": "{HEX}"
                    },
                    {
                        "condition": "ApplyToFileName",
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "doNotReplaceRegex": {
                            "minDigits": 1,
                            "minLetters": 1,
                            "options": 9,
                            "regexStr": "((?<=[-\\._@]|^)[v](\\d+)[\\.](\\d+)[\\.]?(\\d+)?(?=[-\\._@]|$)|((?<=[Bb])2(?=[Bb])))"
                        },
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "NumberInFile",
                        "regex": {
                            "minDigits": 1,
                            "options": 8,
                            "regexStr": "(\\d+)"
                        },
                        "replaceWith": "{N}"
                    },
                    {
                        "createdBy": "AzureDataCatalog",
                        "disableRecursiveReplacerApplication": false,
                        "disabled": false,
                        "lastUpdatedTimestamp": 0,
                        "modifiedBy": "AzureDataCatalog",
                        "name": "Localization",
                        "regex": {
                            "maxLetters": 4,
                            "minLetters": 4,
                            "options": 9,
                            "regexStr": "(?<=[-\\._@]|^)(ar[-_]eg|ar[-_]sa|cy[-_]gb|da[-_]dk|de[-_]at|de[-_]ch|de[-_]de|en[-_]au|en[-_]ca|en[-_]gb|en[-_]ie|en[-_]in|en[-_]my|en[-_]nz|en[-_]ph|en[-_]sg|en[-_]us|en[-_]ww|en[-_]xa|en[-_]za|es[-_]ar|es[-_]cl|es[-_]es|es[-_]mx|es[-_]us|es[-_]xl|fi[-_]fi|fr[-_]be|fr[-_]ca|fr[-_]ch|fr[-_]fr|gu[-_]in|hi[-_]in|id[-_]id|it[-_]it|ja[-_]jp|nb[-_]no|nl[-_]nl|nl[-_]be|pt[-_]br|pt[-_]pt|pl[-_]pl|ru[-_]ru|sv[-_]se|ta[-_]in|te[-_]in|zh[-_]cn|zh[-_]hk|zh[-_]tw|ko[-_]kr|tr[-_]tr)(?=[-\\._@]|$)"
                        },
                        "replaceWith": "{LOC}"
                    }
                ],
                "rejectedPatterns": [],
                "scopedRules": [],
                "version": 5
            }
        }
    ]
}
```
</p>
</details>