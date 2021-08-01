"""
usage: 
    pv management checkNameAvailability --subscriptionId=<val> --accountName=<val>
    pv management createAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payload-file=<val>
    pv management defaultAccount --scopeTenantId=<val> --scopeType=<val> --scope=<val>
    pv management deleteAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management deletePrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
    pv management listKeys --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management listOperations
    pv management listPrivateLinkResources --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> [--groupId=<val>]
    pv management putPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val> --payload-file=<val>
    pv management putResourceGroup --subscriptionId=<val> --resourceGroupName=<val> --location=<val>
    pv management putRoleAssignment --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --roleDefinitionId=<val> --principalId=<val>
    pv management readAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management readAccounts --subscriptionId=<val> [--resourceGroupName=<val>]
    pv management readPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
    pv management readPrivateEndpoints --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management removeDefaultAccount --scopeTenantId=<val> --scopeType=<val> --scope=<val>
    pv management setDefaultAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --scopeTenantId=<val> --scopeType=<val> --scope=<val>
    pv management updateAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payload-file=<val>

options:
    --subscriptionId=<val>                  [string]  The subscription ID.
    --resourceGroupName=<val>               [string]  The name of the resource group.
    --accountName=<val>                     [string]  The name of the account.
    --scopeTenantId=<val>                   [string]  The scope tenant in which the default account is set.
    --scopeType=<val>                       [string]  The scope where the default account is set (Tenant or Subscription).
    --scope=<val>                           [string]  The scope object ID (e.g. sub ID or tenant ID).
    --groupId=<val>                         [string]  The group identifier.
    --privateEndpointConnectionName=<val>   [string]  The name of the private endpoint connection.

mapping:
https://management.azure.com
+--------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                  | Method | Path                                                                                                                                                                             |
+--------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| checkNameAvailability    | POST   | /subscriptions/{subscriptionId}/providers/Microsoft.Purview/checkNameAvailability                                                                                                |
| createAccount            | PUT    | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}                                                            |
| defaultAccount           | GET    | /providers/Microsoft.Purview/getDefaultAccount                                                                                                                                   |
| deleteAccount            | DELETE | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}                                                            |
| deletePrivateEndpoint    | DELETE | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName} |
| listKeys                 | POST   | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/listkeys                                                   |
| listOperations           | GET    | /providers/Microsoft.Purview/operations                                                                                                                                          |
| listPrivateLinkResources | GET    | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateLinkResources/{groupId}                             |
| putPrivateEndpoint       | PUT    | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName} |
| putResourceGroup         | PUT    | /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}                                                                                                               |
| putRoleAssignment        | PUT    | {scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentId}                                                                                                     |
| readAccount              | GET    | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}                                                            |
| readAccounts             | GET    | /subscriptions/{subscriptionId}/providers/Microsoft.Purview/accounts                                                                                                             |
| readPrivateEndpoint      | GET    | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName} |
| readPrivateEndpoints     | GET    | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/privateEndpointConnections                                 |
| removeDefaultAccount     | POST   | /providers/Microsoft.Purview/removeDefaultAccount                                                                                                                                |
| setDefaultAccount        | POST   | /providers/Microsoft.Purview/setDefaultAccount                                                                                                                                   |
| updateAccount            | PATCH  | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}                                                            |
+--------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
