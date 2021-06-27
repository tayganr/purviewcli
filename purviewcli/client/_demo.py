import time, json, string, random
from os import read
from subprocess import Popen, PIPE
from purviewcli.client import settings

def runCommand(cmd):
    print('calling')
    output = Popen(cmd.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0].decode('ascii')
    output = json.loads(output)
    return output


class Demo():
    def demoGenerate(self, args):
        # Init variables
        accountName = None
        nameAvailable = False

        # Generate Azure Purview Account Name
        while nameAvailable == False:
            accountName = 'purview-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            cmd = f"pv management checkNameAvailability --subscriptionId {args['--subscriptionId']} --accountName {accountName}"
            data = runCommand(cmd)
            nameAvailable = data['nameAvailable']
        print(f'Account Name: {accountName}')

        # Provision Resource Group
        resourceGroupName = args['--resourceGroupName'] or 'purview-rg-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        cmd = f"pv management putResourceGroup --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --location {args['--location']}"
        data = runCommand(cmd)
        print(f'Resource Group: {resourceGroupName}')

        # Provision Azure Purview Account
        payload = {
            "identity": {
                "type": "SystemAssigned"
            },
            "location": args['--location'],
            "sku": {
                "name": "Standard",
                "capacity": 4
            }
        }
        with open('temp.json', 'w') as f:
            json.dump(payload, f)
        print('[WORKING] Provisioning Azure Purview account...')
        cmd = f"pv management createAccount --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --accountName {accountName} --payload-file temp.json"
        data = runCommand(cmd)

        # Check provisioningState until Succeeded
        provisioning = True
        while provisioning:
            time.sleep(30)
            cmd = f"pv management readAccount --subscriptionId {args['--subscriptionId']} --resourceGroupName {resourceGroupName} --accountName {accountName}"
            data = runCommand(cmd)
            if data['properties']['provisioningState'] == 'Succeeded':
                provisioning = False

        catalogEndpoint = data['properties']['endpoints']['catalog']

        response = { 'x': 'y' }
        return response
