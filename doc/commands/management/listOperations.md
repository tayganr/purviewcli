# pv management listOperations
[Command Reference](../../../README.md#command-reference) > [management](./main.md) > listOperations

## Description
Lists the available operations

## Syntax
```
pv management listOperations
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Operations > [List](https://docs.microsoft.com/en-us/rest/api/purview/operations/list)
```
GET https://management.azure.com/providers/Microsoft.Purview/operations
```

## Examples
List the operations available via the Azure Purview resource provider.
```powershell
pv management listOperations
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "value": [
        {
            "display": {
                "description": "Reads all available operations for Microsoft Purview provider.",
                "operation": "Read all operations",
                "provider": "Microsoft Purview",
                "resource": "Operations"
            },
            "name": "Microsoft.Purview/operations/read"
        },
        {
            "display": {
                "description": "Register the subscription for Microsoft Purview provider.",
                "operation": "Register the Microsoft Purview provider",
                "provider": "Microsoft Purview",
                "resource": "Microsoft Purview provider"
            },
            "name": "Microsoft.Purview/register/action"
        },
        {
            "display": {
                "description": "Unregister the subscription for Microsoft Purview provider.",
                "operation": "Unregister the Microsoft Purview provider",
                "provider": "Microsoft Purview",
                "resource": "Microsoft Purview provider"
            },
            "name": "Microsoft.Purview/unregister/action"
        },
        {
            "display": {
                "description": "Gets the default account for the scope.",
                "operation": "Get Default Account",
                "provider": "Microsoft Purview",
                "resource": "Tenant"
            },
            "name": "Microsoft.Purview/getDefaultAccount/read"
        },
        {
            "display": {
                "description": "Sets the default account for the scope.",
                "operation": "Set Default Account",
                "provider": "Microsoft Purview",
                "resource": "Tenant"
            },
            "name": "Microsoft.Purview/setDefaultAccount/action"
        },
        {
            "display": {
                "description": "Removes the default account for the scope.",
                "operation": "Removes Default Account",
                "provider": "Microsoft Purview",
                "resource": "Tenant"
            },
            "name": "Microsoft.Purview/removeDefaultAccount/action"
        },
        {
            "display": {
                "description": "Check if name of purview account resource is available for Microsoft Purview provider.",
                "operation": "Check if name of purview account is available",
                "provider": "Microsoft Purview",
                "resource": "Check Name Availability"
            },
            "name": "Microsoft.Purview/checknameavailability/read"
        },
        {
            "display": {
                "description": "Read account resource for Microsoft Purview provider.",
                "operation": "Read account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/read"
        },
        {
            "display": {
                "description": "Write account resource for Microsoft Purview provider.",
                "operation": "Write account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/write"
        },
        {
            "display": {
                "description": "Delete account resource for Microsoft Purview provider.",
                "operation": "Delete account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/delete"
        },
        {
            "display": {
                "description": "List keys on the account resource for Microsoft Purview provider.",
                "operation": "List keys on the account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/listkeys/action"
        },
        {
            "display": {
                "description": "Add root collection admin to account resource for Microsoft Purview provider.",
                "operation": "Add root collection admin to account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/addrootcollectionadmin/action"
        },
        {
            "display": {
                "description": "Read the operation status on the account resource for Microsoft Purview provider.",
                "operation": "Read the operation status on the account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/operationresults/read"
        },
        {
            "display": {
                "description": "Move account resource for Microsoft Purview provider.",
                "operation": "Move account resource",
                "provider": "Microsoft Purview",
                "resource": "Account"
            },
            "name": "Microsoft.Purview/accounts/move/action"
        },
        {
            "display": {
                "description": "Monitor async operations.",
                "operation": "Operation result by location",
                "provider": "Microsoft Purview",
                "resource": "Operation Result"
            },
            "name": "Microsoft.Purview/locations/operationResults/read"
        },
        {
            "display": {
                "description": "Read Account Link Resources.",
                "operation": "Read Link Resources",
                "provider": "Microsoft Purview",
                "resource": "Private Link Resources"
            },
            "name": "Microsoft.Purview/accounts/privatelinkresources/read"
        },
        {
            "display": {
                "description": "Read Account Private Endpoint Connection Proxy.",
                "operation": "Read Private Endpoint Connection Proxy",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection Proxy"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnectionProxies/read"
        },
        {
            "display": {
                "description": "Write Account Private Endpoint Connection Proxy.",
                "operation": "Write Private Endpoint Connection Proxy",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection Proxy"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnectionProxies/write"
        },
        {
            "display": {
                "description": "Delete Account Private Endpoint Connection Proxy.",
                "operation": "Delete Private Endpoint Connection Proxy",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection Proxy"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnectionProxies/delete"
        },
        {
            "display": {
                "description": "Monitor Private Endpoint Connection Proxy async operations.",
                "operation": "Operation result by Private Endpoint Connection Proxy",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection Proxy Operation Result"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnectionProxies/operationResults/read"
        },
        {
            "display": {
                "description": "Validate Account Private Endpoint Connection Proxy.",
                "operation": "Validate Private Endpoint Connection Proxy",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection Proxy"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnectionProxies/validate/action"
        },
        {
            "display": {
                "description": "Read Private Endpoint Connection.",
                "operation": "Read Private Endpoint Connection",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnections/read"
        },
        {
            "display": {
                "description": "Create or update Private Endpoint Connection.",
                "operation": "Create or update Private Endpoint Connection",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnections/write"
        },
        {
            "display": {
                "description": "Delete Private Endpoint Connection.",
                "operation": "Delete Private Endpoint Connection",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection"
            },
            "name": "Microsoft.Purview/accounts/privateEndpointConnections/delete"
        },
        {
            "display": {
                "description": "Approve Private Endpoint Connection.",
                "operation": "Approve Private Endpoint Connection",
                "provider": "Microsoft Purview",
                "resource": "Private Endpoint Connection"
            },
            "name": "Microsoft.Purview/accounts/PrivateEndpointConnectionsApproval/action"
        },
        {
            "display": {
                "description": "Permission is deprecated.",
                "operation": "Deprecated",
                "provider": "Microsoft Purview",
                "resource": "Data Plane"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/accounts/data/read"
        },
        {
            "display": {
                "description": "Permission is deprecated.",
                "operation": "Deprecated",
                "provider": "Microsoft Purview",
                "resource": "Data Plane"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/accounts/data/write"
        },
        {
            "display": {
                "description": "Permission is deprecated.",
                "operation": "Deprecated",
                "provider": "Microsoft Purview",
                "resource": "Data Scan"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/accounts/scan/read"
        },
        {
            "display": {
                "description": "Permission is deprecated.",
                "operation": "Deprecated",
                "provider": "Microsoft Purview",
                "resource": "Data Scan"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/accounts/scan/write"
        },
        {
            "display": {
                "description": "Read Policy Element.",
                "operation": "Read Policy Element",
                "provider": "Microsoft Purview",
                "resource": "Policy element"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/policyElements/read"
        },
        {
            "display": {
                "description": "Create or update Policy Element.",
                "operation": "Create or update Policy Element",
                "provider": "Microsoft Purview",
                "resource": "Policy element"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/policyElements/write"
        },
        {
            "display": {
                "description": "Delete Policy Element.",
                "operation": "Delete Policy Element",
                "provider": "Microsoft Purview",
                "resource": "Policy element"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/policyElements/delete"
        },
        {
            "display": {
                "description": "Read Attribute Blob.",
                "operation": "Read Attribute Blob",
                "provider": "Microsoft Purview",
                "resource": "Attribute Blob"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/attributeBlobs/read"
        },
        {
            "display": {
                "description": "Write Attribute Blob.",
                "operation": "Write Attribute Blob",
                "provider": "Microsoft Purview",
                "resource": "Attribute Blob"
            },
            "isDataAction": true,
            "name": "Microsoft.Purview/attributeBlobs/write"
        },
        {
            "display": {
                "description": "Gets the available metrics for the catalog.",
                "operation": "Read metric definitions",
                "provider": "Microsoft Purview",
                "resource": "Metric definitions"
            },
            "name": "Microsoft.Purview/accounts/providers/Microsoft.Insights/metricDefinitions/read",
            "origin": "system",
            "properties": {
                "serviceSpecification": {
                    "metricSpecifications": [
                        {
                            "aggregationType": "Total",
                            "dimensions": [
                                {
                                    "displayName": "ResourceId",
                                    "name": "ResourceId",
                                    "toBeExportedForCustomer": true
                                }
                            ],
                            "displayDescription": "Indicates the scan billing units.",
                            "displayName": "Scan Billing Units",
                            "enableRegionalMdmAccount": "true",
                            "internalMetricName": "ScanBillingUnits",
                            "name": "ScanBillingUnits",
                            "sourceMdmNamespace": "CatalogAnalytics",
                            "supportedAggregationTypes": [
                                "Total"
                            ],
                            "supportedTimeGrainTypes": [
                                "PT1M",
                                "PT15M",
                                "PT1H",
                                "P1D"
                            ],
                            "unit": "Count"
                        },
                        {
                            "aggregationType": "Total",
                            "dimensions": [
                                {
                                    "displayName": "ResourceId",
                                    "name": "ResourceId",
                                    "toBeExportedForCustomer": true
                                }
                            ],
                            "displayDescription": "Indicates the number of scans cancelled.",
                            "displayName": "Scan Cancelled",
                            "enableRegionalMdmAccount": "true",
                            "internalMetricName": "ScanCancelled",
                            "name": "ScanCancelled",
                            "sourceMdmNamespace": "CatalogAnalytics",
                            "supportedAggregationTypes": [
                                "Total",
                                "Count"
                            ],
                            "supportedTimeGrainTypes": [
                                "PT1M",
                                "PT15M",
                                "PT1H",
                                "P1D"
                            ],
                            "unit": "Count"
                        },
                        {
                            "aggregationType": "Total",
                            "dimensions": [
                                {
                                    "displayName": "ResourceId",
                                    "name": "ResourceId",
                                    "toBeExportedForCustomer": true
                                }
                            ],
                            "displayDescription": "Indicates the number of scans completed successfully.",
                            "displayName": "Scan Completed",
                            "enableRegionalMdmAccount": "true",
                            "internalMetricName": "ScanCompleted",
                            "name": "ScanCompleted",
                            "sourceMdmNamespace": "CatalogAnalytics",
                            "supportedAggregationTypes": [
                                "Total",
                                "Count"
                            ],
                            "supportedTimeGrainTypes": [
                                "PT1M",
                                "PT15M",
                                "PT1H",
                                "P1D"
                            ],
                            "unit": "Count"
                        },
                        {
                            "aggregationType": "Total",
                            "dimensions": [
                                {
                                    "displayName": "ResourceId",
                                    "name": "ResourceId",
                                    "toBeExportedForCustomer": true
                                }
                            ],
                            "displayDescription": "Indicates the number of scans failed.",
                            "displayName": "Scan Failed",
                            "enableRegionalMdmAccount": "true",
                            "internalMetricName": "ScanFailed",
                            "name": "ScanFailed",
                            "sourceMdmNamespace": "CatalogAnalytics",
                            "supportedAggregationTypes": [
                                "Total",
                                "Count"
                            ],
                            "supportedTimeGrainTypes": [
                                "PT1M",
                                "PT15M",
                                "PT1H",
                                "P1D"
                            ],
                            "unit": "Count"
                        },
                        {
                            "aggregationType": "Total",
                            "dimensions": [
                                {
                                    "displayName": "ResourceId",
                                    "name": "ResourceId",
                                    "toBeExportedForCustomer": true
                                }
                            ],
                            "displayDescription": "Indicates the total scan time in seconds.",
                            "displayName": "Scan time taken",
                            "enableRegionalMdmAccount": "true",
                            "internalMetricName": "ScanTimeTaken",
                            "name": "ScanTimeTaken",
                            "sourceMdmNamespace": "CatalogAnalytics",
                            "supportedAggregationTypes": [
                                "Minimum",
                                "Maximum",
                                "Total",
                                "Average"
                            ],
                            "supportedTimeGrainTypes": [
                                "PT1M",
                                "PT15M",
                                "PT1H",
                                "P1D"
                            ],
                            "unit": "Seconds"
                        }
                    ]
                }
            }
        },
        {
            "display": {
                "description": "Gets the available logs for the catalog.",
                "operation": "Read log definitions",
                "provider": "Microsoft Purview",
                "resource": "Log definitions"
            },
            "name": "Microsoft.Purview/accounts/providers/Microsoft.Insights/logDefinitions/read",
            "origin": "system",
            "properties": {
                "serviceSpecification": {
                    "logSpecifications": [
                        {
                            "blobDuration": "PT1H",
                            "displayName": "ScanStatus",
                            "name": "ScanStatusLogEvent"
                        }
                    ]
                }
            }
        },
        {
            "display": {
                "description": "Gets the diagnostic setting for the resource.",
                "operation": "Read diagnostic setting",
                "provider": "Microsoft Purview",
                "resource": "Diagnostic settings"
            },
            "name": "Microsoft.Purview/accounts/providers/Microsoft.Insights/diagnosticSettings/read",
            "origin": "system"
        },
        {
            "display": {
                "description": "Creates or updates the diagnostic setting for the resource.",
                "operation": "Write diagnostic setting",
                "provider": "Microsoft Purview",
                "resource": "Diagnostic setting"
            },
            "name": "Microsoft.Purview/accounts/providers/Microsoft.Insights/diagnosticSettings/write",
            "origin": "system"
        }
    ]
}
```
</p>
</details>