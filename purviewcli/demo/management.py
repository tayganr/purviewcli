import random, string, uuid, time, sys
from purviewcli.demo.utils import Utils

class ControlPlane():
    def __init__(self):
        self.token = Utils.get_token('management')
        self.tokenGraph = Utils.get_token('graph')

    # RESOURCE GROUP
    def resourceGroupCheckExistence(self, subscriptionId, resourceGroupName):
        method = 'HEAD'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = {'api-version': '2021-04-01'}
        payload = None
        data = Utils.http_get(method, endpoint, params, payload, self.token)
        response = True if data['status_code'] == 204 else False
        return response

    def resourceGroupCreateUpdate(self, subscriptionId, resourceGroupName, location):
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = { 'api-version': '2021-04-01' }
        payload = { 'location': location }
        data = Utils.http_get(method, endpoint, params, payload, self.token)      
        return data

    def resourceGroupGet(self, subscriptionId, resourceGroupName):
        method = 'GET'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = {'api-version': '2021-04-01'}
        payload = None
        data = Utils.http_get(method, endpoint, params, payload, self.token)
        return data

    def resourceGroupProvision(self, subscriptionId, resourceGroupName, location):
        # 1. Set resourceGroupName
        resourceGroupName = resourceGroupName or 'purview-rg-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # 2. Create resourceGroupName if does not exists
        isExists = self.resourceGroupCheckExistence(subscriptionId, resourceGroupName)
        if isExists:
            print(f'Will use existing resource group: [{resourceGroupName}]')
        else:
            print(f'Creating new resource group: [{resourceGroupName}]...')
            data = self.resourceGroupCreateUpdate(subscriptionId, resourceGroupName, location)
            if 'error' in data:
                print(data)
                sys.exit()

            provisioning = True
            while provisioning:
                if data['properties']['provisioningState'] == 'Succeeded':
                    provisioning = False
                else:
                    data = self.resourceGroupGet(subscriptionId, resourceGroupName)
            print(f'Resource group [{resourceGroupName}] created successfully!')

    def provisionStorageAccount(self, subscriptionId, location, resourceGroupName, token):
        accountName = 'adls' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'
        params = { 'api-version': '2018-02-01' }
        payload = {
            "sku": {
                "name": "Standard_LRS"
            },
            "properties": {
                "isHnsEnabled": True
            },
            "kind": "StorageV2",
            "location": location,
        }
        data = Utils.http_get(method, endpoint, params, payload, token)
        print(f'ADLS Gen2 Storage Account: {accountName}')
        return accountName

    def provisionAccount(self, subscriptionId, location, resourceGroupName, token):
        # Generate unique name
        accountName = None
        nameAvailable = False
        while nameAvailable == False:
            accountName = 'purview-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            method = 'POST'
            endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Purview/checkNameAvailability'
            params = {'api-version': '2020-12-01-preview'}
            payload = {'name': accountName, 'type': 'Microsoft.Purview/accounts'}
            data = Utils.http_get(method, endpoint, params, payload, token)
            nameAvailable = data['nameAvailable']
        print(f'Account Name: {accountName}')

        # Provision Azure Purview Account
        print('Provisioning Azure Purview account...')
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        params = {'api-version': '2020-12-01-preview'}
        payload = {
            "identity": {
                "type": "SystemAssigned"
            },
            "location": location,
            "sku": {
                "name": "Standard",
                "capacity": 4
            }
        }
        data = Utils.http_get(method, endpoint, params, payload, token)

        # Check provisioningState until Succeeded
        time.sleep(60)
        provisioning = True
        while provisioning:
            time.sleep(5)
            method = 'GET'
            endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
            params = {'api-version': '2020-12-01-preview'}
            payload = None
            data = Utils.http_get(method, endpoint, params, payload, token)
            if data['properties']['provisioningState'] == 'Succeeded':
                provisioning = False

        print(f'Ready! Purview Studio: https://ms.web.purview.azure.com/resource/{accountName}')
        return accountName

    def getMe(self, token):
        method = 'GET'
        endpoint = 'https://graph.microsoft.com/v1.0/me'
        params = None
        payload = None
        data = Utils.http_get(method, endpoint, params, payload, token)
        principalId = data['id']
        userPrincipalName = data['userPrincipalName']
        return principalId, userPrincipalName

    def assignRole(self, subscriptionId, resourceGroupName, accountName, roleDefinitionId, principalId, token):
        method = 'PUT'
        scope = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        roleAssignmentId = uuid.uuid4()
        endpoint = f'{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentId}?api-version=2015-07-01'
        roleDefinitionId = roleDefinitionId
        params = None
        payload = {
            "properties": {
                "roleDefinitionId": f"/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId}",
                "principalId": f'{principalId}'
            }
        }
        data = Utils.http_get(method, endpoint, params, payload, token)