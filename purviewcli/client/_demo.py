import math
from datetime import datetime
from purviewcli.demo.utils import Utils
from purviewcli.demo.management import ControlPlane
from purviewcli.demo.purview import DataPlane

class Demo():

    def __init__(self):
        self.token_purview = Utils.get_token('purview')
        self.token_management = Utils.get_token('management')
        self.token_graph = Utils.get_token('graph')

    def demoGenerate(self, args):
        # Init variables
        resourceGroupName = args['--resourceGroupName']
        subscriptionId = args['--subscriptionId']
        location = args['--location']

        # Start Timestamp
        startTime = datetime.now()

        # Provision Resources
        resourceGroupName = ControlPlane.provisionResourceGroup(subscriptionId, location, resourceGroupName, self.token_management)
        accountName = ControlPlane.provisionAccount(subscriptionId, location, resourceGroupName, self.token_management)

        # Add Role Assignment (Owner)
        principalId, userPrincipalName = ControlPlane.getMe(self.token_graph)
        print(f'Assigning role [User Access Administrator] to [principalId: {principalId}; userPrincipalName: {userPrincipalName}]')
        roleDefinitionId = '18d7d88d-d35e-4fb5-a5c3-7773c20a72d9' # User Access Administrator
        ControlPlane.assignRole(subscriptionId, resourceGroupName, accountName, roleDefinitionId, principalId, self.token_management)
        
        # Populate account
        print('Populating environment...')
        DataPlane.populateTypes(accountName, self.token_purview)
        DataPlane.populateEntities(accountName, self.token_purview, args)
        DataPlane.populateSources(accountName, self.token_purview)
        
        # Complete
        print('Complete!')

        # Calculate Total Duration
        finishTime = datetime.now()
        duration = finishTime - startTime
        minutes = math.floor(duration.seconds / 60)
        seconds = duration.seconds % 60
        print(f'Duration: {minutes:02}:{seconds:02}')
        
        response = ' '
        return response
