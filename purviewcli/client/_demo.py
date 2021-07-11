import math, jwt, sys, random, json
from datetime import datetime
from purviewcli.demo.management import ControlPlane
from purviewcli.demo.purview import DataPlane
from purviewcli.demo.utils import get_token

class Demo():

    def demoGenerate(self, args):
        # Start Timestamp
        startTime = datetime.now()

        # Init variables
        resourceGroupName = args['--resourceGroupName']
        subscriptionId = args['--subscriptionId']
        location = args['--location']
        accountName = args['--accountName']
        peopleFile = args['--peopleFile']
        cp = ControlPlane()
        dp = DataPlane()

        # Get Tokens
        cp.token = get_token('management')
        if cp.token is None:
            sys.exit()
        else:
            cp.tokenGraph = get_token('graph')
            dp.token = get_token('purview')

        # Decode JWT
        print('\n=================[CREDENTIALS]=================')
        tokenManagement = cp.token
        claimset = jwt.decode(tokenManagement, options={"verify_signature": False})
        name = claimset['name']
        principalId = claimset ['oid']
        userPrincipalName = claimset['upn']
        tenantId = claimset['tid']
        print(f' - Tenant ID:\t\t{tenantId}')
        print(f' - Object ID:\t\t{principalId}')
        print(f' - Name:\t\t{name}')
        print(f' - Principal Name:\t{userPrincipalName}')

        # Subscription
        print('\n=================[SUBSCRIPTION]=================')
        subscriptionsList = cp.subscriptionsList()
        subscriptions = []
        subscriptionName = {}
        for sub in subscriptionsList:
            subscriptions.append(sub['id'])
            subscriptionName[sub['id']] = sub['name']
            if sub['isDefault'] == True:
                defaultSubscriptionId = sub['id']
        if subscriptionId is None:
            subscriptionId = defaultSubscriptionId
        elif subscriptionId in subscriptions:
            pass
        else:
            print(f' - The current set of credentials does not have access to Subscription ID: {subscriptionId}\n')
            sys.exit()
        print(f' - Subscription ID:\t{subscriptionId}')
        print(f' - Subscription Name:\t{subscriptionName[subscriptionId]}')

        # Location
        if location == None:
            print('\n=================[LOCATION]=================')
            print(' - No location was specified, retrieving a list of valid locations...')
            resourceProviderNamespace = 'Microsoft.Purview'
            provider = cp.providersGet(subscriptionId, resourceProviderNamespace)
            for resourceType in provider['resourceTypes']:
                if resourceType['resourceType'] == 'accounts':
                    locations = resourceType['locations']
                    location = random.choice(locations)
                    print(f' - Resources will be deployed to {location}')

        # Provision Resources
        print('\n=================[RESOURCE GROUP]=================')
        resourceGroupName = cp.resourceGroupProvision(subscriptionId, resourceGroupName, location)

        print('\n=================[PURVIEW ACCOUNT]=================')
        accountName = cp.purviewAccountProvision(subscriptionId, location, resourceGroupName, accountName)

        # Add Role Assignment (Owner)
        print('\n=================[ACCESS CONTROL]=================')
        scope = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        roleDefinitionId = '18d7d88d-d35e-4fb5-a5c3-7773c20a72d9' # User Access Administrator
        principalId, userPrincipalName = cp.getMe()
        print(f' - Assigning role [User Access Administrator] to [principalId: {principalId}; userPrincipalName: {userPrincipalName}]')
        cp.roleAssignmentCreate(scope, roleDefinitionId, principalId)

        # Validate Contacts (peopleFile)
        if peopleFile:
            with open(peopleFile) as f:
                people = json.load(f)
            sampleId = people['value'][0]['id']
            sampleTest = cp.getUser(sampleId)
            if 'error' in sampleTest:
                print(f' - Warning: The peopleFile located at {peopleFile} is invalid. Contacts were not able to be found within tenant {tenantId}.')
                peopleFile = None
        
        # Populate account
        print('\n=================[HYDRATING ENVIRONMENT]=================')
        dp.populateTypes(accountName)
        dp.populateEntities(accountName, peopleFile)
        dp.populateSources(accountName)
        
        # Complete
        print('\n=================[COMPLETE]=================')
        # Calculate Total Duration
        finishTime = datetime.now()
        duration = finishTime - startTime
        minutes = math.floor(duration.seconds / 60)
        seconds = duration.seconds % 60
        print(f' - Duration: {minutes:02}:{seconds:02}')
        
        response = ' '
        return response
