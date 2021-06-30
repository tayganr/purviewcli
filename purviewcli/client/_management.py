import uuid
from .endpoint import Endpoint, decorator, get_json

class Management(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'management'

    # https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
    @decorator
    def managementPutRoleAssignment(self, args):
        self.method = 'PUT'
        scope = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}'
        roleAssignmentId = uuid.uuid4()
        self.endpoint = f'{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentId}?api-version=2015-07-01'
        roleDefinitionId = args["--roleDefinitionId"]
        self.payload = {
            "properties": {
                "roleDefinitionId": f"/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId}",
                "principalId": f'{args["--principalId"]}'
            }
        }

    @decorator
    def managementPutResourceGroup(self, args):
        self.method = 'PUT'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourcegroups/{args["--resourceGroupName"]}'
        self.params = { 'api-version': '2021-04-01' }
        self.payload = { 'location': args["--location"] }

    @decorator
    def managementListOperations(self, args):
        self.method = 'GET'
        self.endpoint = '/providers/Microsoft.Purview/operations'
        self.params = {'api-version': '2020-12-01-preview'}
   
    @decorator
    def managementCheckNameAvailability(self, args):
        self.method = 'POST'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/providers/Microsoft.Purview/checkNameAvailability'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = {'name': args['--accountName'], 'type': 'Microsoft.Purview/accounts'}
    
    @decorator
    def managementReadAccounts(self, args):
        self.method = 'GET'
        if args["--resourceGroupName"] is None:
            self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/providers/Microsoft.Purview/accounts'
        else:
            self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts'
        self.params = {'api-version': '2020-12-01-preview'}

    @decorator
    def managementReadAccount(self, args):
        self.method = 'GET'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementCreateAccount(self, args):
        self.method = 'PUT'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = get_json(args, '--payload-file')
    
    @decorator
    def managementDeleteAccount(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementListKeys(self, args):
        self.method = 'POST'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/listkeys'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementUpdateAccount(self, args):
        self.method = 'PATCH'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = get_json(args, '--payload-file')

    @decorator
    def managementDefaultAccount(self, args):
        self.method = 'GET'
        self.endpoint = f'/providers/Microsoft.Purview/getDefaultAccount'
        self.params = {'scopeTenantId': args["--scopeTenantId"], 'scopeType': args["--scopeType"], 'scope': args["--scope"], 'api-version': '2020-12-01-preview'}

    @decorator
    def managementSetDefaultAccount(self, args):
        self.method = 'POST'
        self.endpoint = '/providers/Microsoft.Purview/setDefaultAccount'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = {
            "scopeTenantId": args["--scopeTenantId"],
            "scopeType": args["--scopeType"],
            "scope": args["--scope"],
            "accountName": args["--accountName"],
            "resourceGroupName": args["--resourceGroupName"],
            "subscriptionId": args["--subscriptionId"]
        }
    
    @decorator
    def managementRemoveDefaultAccount(self, args):
        self.method = 'POST'
        self.endpoint = '/providers/Microsoft.Purview/removeDefaultAccount'
        self.params = {'scopeTenantId': args["--scopeTenantId"], 'scopeType': args["--scopeType"], 'scope': args["--scope"], 'api-version': '2020-12-01-preview'}

    @decorator
    def managementListPrivateLinkResources(self, args):
        self.method = 'GET'
        if args["--groupId"] is None:
            self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateLinkResources'
        else:
            self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateLinkResources/{args["--groupId"]}'
        self.params = {'api-version': '2020-12-01-preview'}

    @decorator
    def managementPutPrivateEndpoint(self, args):
        self.method = 'PUT'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections/{args["--privateEndpointConnectionName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = get_json(args, '--payload-file')
    
    @decorator
    def managementDeletePrivateEndpoint(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections/{args["--privateEndpointConnectionName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementReadPrivateEndpoint(self, args):
        self.method = 'GET'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections/{args["--privateEndpointConnectionName"]}'
        self.params = {'api-version': '2020-12-01-preview'}

    @decorator
    def managementReadPrivateEndpoints(self, args):
        self.method = 'GET'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections'
        self.params = {'api-version': '2020-12-01-preview'}
