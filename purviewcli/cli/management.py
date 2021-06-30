"""
usage: 
    pv management listOperations
    pv management checkNameAvailability --subscriptionId=<val> --accountName=<val>
    pv management putResourceGroup --subscriptionId=<val> --resourceGroupName=<val> --location=<val>
    pv management putRoleAssignment --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --roleDefinitionId=<val> --principalId=<val>
    pv management createAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payload-file=<val>
    pv management updateAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --payload-file=<val>
    pv management deleteAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management readAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management readAccounts --subscriptionId=<val> [--resourceGroupName=<val>]
    pv management listKeys --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>
    pv management defaultAccount --scopeTenantId=<val> --scopeType=<val> --scope=<val>
    pv management setDefaultAccount --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --scopeTenantId=<val> --scopeType=<val> --scope=<val>
    pv management removeDefaultAccount --scopeTenantId=<val> --scopeType=<val> --scope=<val>
    pv management listPrivateLinkResources --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> [--groupId=<val>]
    pv management putPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val> --payload-file=<val>
    pv management deletePrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
    pv management readPrivateEndpoint --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val> --privateEndpointConnectionName=<val>
    pv management readPrivateEndpoints --subscriptionId=<val> --resourceGroupName=<val> --accountName=<val>

options:
    --subscriptionId=<val>                  [string]  The subscription ID.
    --resourceGroupName=<val>               [string]  The name of the resource group.
    --accountName=<val>                     [string]  The name of the account.
    --scopeTenantId=<val>                   [string]  The scope tenant in which the default account is set.
    --scopeType=<val>                       [string]  The scope where the default account is set (Tenant or Subscription).
    --scope=<val>                           [string]  The scope object ID (e.g. sub ID or tenant ID).
    --groupId=<val>                         [string]  The group identifier.
    --privateEndpointConnectionName=<val>   [string]  The name of the private endpoint connection.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
