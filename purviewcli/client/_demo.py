import math, jwt, sys, random, json, string
from datetime import datetime
from purviewcli.demo.management import ControlPlane
from purviewcli.demo.purview import DataPlane
from purviewcli.demo.utils import get_token

def printHeading(heading):
    print('\n-------------------------------------------------------------------------')
    print(f' {heading}')
    print('-------------------------------------------------------------------------')

# def setTokens()

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
        printHeading('CREDENTIALS')
        tokenManagement = cp.token
        claimset = jwt.decode(tokenManagement, options={"verify_signature": False})
        name = claimset['name']
        principalId = claimset ['oid']
        tenantId = claimset['tid']
        print(f' - Tenant ID:\t\t{tenantId}')
        print(f' - Subscription ID:\t{subscriptionId}')
        print(f' - Object ID:\t\t{principalId}')
        print(f' - Name:\t\t{name}')

        # Subscription
        # printHeading('SUBSCRIPTION')
        # subscriptionsList = cp.subscriptionsList()
        # subscriptions = []
        # subscriptionName = {}
        # for sub in subscriptionsList:
        #     subscriptions.append(sub['id'])
        #     subscriptionName[sub['id']] = sub['name']
        #     if sub['isDefault'] == True:
        #         defaultSubscriptionId = sub['id']
        # if subscriptionId is None:
        #     subscriptionId = defaultSubscriptionId
        # elif subscriptionId in subscriptions:
        #     pass
        # else:
        #     print(f' - The current set of credentials does not have access to Subscription ID: {subscriptionId}\n')
        #     sys.exit()
        # print(f' - Subscription ID:\t{subscriptionId}')
        # print(f' - Subscription Name:\t{subscriptionName[subscriptionId]}')

        # Location
        if location == None:
            printHeading('LOCATION')
            print(' - No location was specified, retrieving a list of valid locations...')
            resourceProviderNamespace = 'Microsoft.Purview'
            provider = cp.providersGet(subscriptionId, resourceProviderNamespace)
            for resourceType in provider['resourceTypes']:
                if resourceType['resourceType'] == 'accounts':
                    locations = resourceType['locations']
                    location = random.choice(locations)
                    print(f' - Resources will be deployed to {location}')

        # Provision Resources
        printHeading('RESOURCE GROUP')
        resourceGroupName = cp.resourceGroupProvision(subscriptionId, resourceGroupName, location)

        printHeading('PURVIEW ACCOUNT')
        account = cp.purviewAccountProvision(subscriptionId, location, resourceGroupName, accountName)
        accountName = account['name']
        purviewManagedIdentity = account['identity']['principalId']

        # Provision Azure Storage Account
        printHeading('STORAGE ACCOUNT')
        # 1. Create Storage Acount
        storage = cp.storageAccountProvision(subscriptionId, location, resourceGroupName)
        storageAccountName = storage['name']
        # 2. Get Storage Key
        storageAccountKey = cp.storageAccountGetKey(subscriptionId, resourceGroupName, storageAccountName)
        # 3. Assign Storage Blob Data Reader role to Azure Purview Managed Identity
        scope = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{storageAccountName}'
        roleDefinitionId = '2a2b9908-6ea1-4ae2-8e65-a410df84e7d1' # Storage Blob Data Reader
        print(f' - Assigning role [Storage Blob Data Reader] to Azure Purview Managed Identity (principalId [{purviewManagedIdentity}]).')
        cp.roleAssignmentCreate(scope, roleDefinitionId, purviewManagedIdentity)
        # 4. Populate Storage Account with sample data
        print(f' - Uploading sample data to Azure Data Lake Storage...')
        cp.storagePopulate(storageAccountName, storageAccountKey)

        printHeading('DATA MAP')
        # 5. Register Source
        dataSourceName = storageAccountName
        sourcePayload = {
            "id": "datasources/AdlsGen2",
            "kind": "AdlsGen2",
            "name": storageAccountName,
            "properties": {
                "endpoint": f"https://{storageAccountName}.dfs.core.windows.net/",
                "location": location,
                "resourceGroup": resourceGroupName,
                "resourceName": storageAccountName,
                "subscriptionId": subscriptionId
            }
        }
        print(f' - Registering Azure Data Lake Storage Gen2 Data Source [{dataSourceName}].')
        dp.registerSource(accountName, dataSourceName, sourcePayload)
        # 6. Create Scan
        scanName = 'Scan-' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=3))
        scanPayload = {
            "properties":{
                "scanRulesetName": "AdlsGen2",
                "scanRulesetType": "System"
            },
            "kind": "AdlsGen2Msi",
            "id": f"datasources/{dataSourceName}/scans/{scanName}",
            "name": scanName
        }
        print(f' - Creating Scan [{scanName}].')
        dp.createScan(accountName, dataSourceName, scanName, scanPayload)
        # 7. Trigger Scan
        print(f' - Triggering Run...')
        dp.runScan(accountName, dataSourceName, scanName)

        # Add Role Assignment (Owner)
        printHeading('ACCESS CONTROL')
        scope = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        roleDefinitionId = '18d7d88d-d35e-4fb5-a5c3-7773c20a72d9' # User Access Administrator
        print(f' - Assigning role [User Access Administrator] to [principalId: {principalId}; name: {name}]')
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
        printHeading('HYDRATING ENVIRONMENT')
        dp.populateTypes(accountName)
        dp.populateEntities(accountName, peopleFile)
        dp.populateSources(accountName)
        
        # Complete
        printHeading('COMPLETE')
        # Calculate Total Duration
        finishTime = datetime.now()
        duration = finishTime - startTime
        minutes = math.floor(duration.seconds / 60)
        seconds = duration.seconds % 60
        print(f' - Duration: {minutes:02}:{seconds:02}')
        
        response = ' '
        return response
