import math
from datetime import datetime
from purviewcli.demo.management import ControlPlane
from purviewcli.demo.purview import DataPlane

class Demo():

    def demoGenerate(self, args):
        # Init variables
        resourceGroupName = args['--resourceGroupName']
        subscriptionId = args['--subscriptionId']
        location = args['--location']
        accountName = args['--accountName']
        peopleFile = args['--peopleFile']
        cp = ControlPlane()
        dp = DataPlane()

        # Start Timestamp
        startTime = datetime.now()

        # Provision Resources
        print('\n==============[RESOURCE GROUP]==============')
        resourceGroupName = cp.resourceGroupProvision(subscriptionId, resourceGroupName, location)

        print('\n==============[PURVIEW ACCOUNT]==============')
        accountName = cp.purviewAccountProvision(subscriptionId, location, resourceGroupName, accountName)

        # Add Role Assignment (Owner)
        print('\n==============[ACCESS CONTROL]==============')
        scope = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        roleDefinitionId = '18d7d88d-d35e-4fb5-a5c3-7773c20a72d9' # User Access Administrator
        principalId, userPrincipalName = cp.getMe()
        print(f' - Assigning role [User Access Administrator] to [principalId: {principalId}; userPrincipalName: {userPrincipalName}]')
        cp.roleAssignmentCreate(scope, roleDefinitionId, principalId)
        
        # Populate account
        print('\n==============[HYDRATING ENVIRONMENT]==============')
        dp.populateTypes(accountName)
        dp.populateEntities(accountName, peopleFile)
        dp.populateSources(accountName)
        
        # Complete
        print('\n==============[COMPLETE]==============')
        # Calculate Total Duration
        finishTime = datetime.now()
        duration = finishTime - startTime
        minutes = math.floor(duration.seconds / 60)
        seconds = duration.seconds % 60
        print(f' - Duration: {minutes:02}:{seconds:02}')
        
        response = ' '
        return response
