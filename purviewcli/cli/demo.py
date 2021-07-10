"""
usage: 
    pv demo generate [--subscriptionId=<val> --resourceGroupName=<val> --location=<val> --accountName=<val> --peopleFile=<val>]

options:
    --subscriptionId=<val>                  [string]  An Azure Subscription ID.
    --location=<val>                        [string]  A valid Azure Purview resource location.
    --resourceGroupName=<val>               [string]  (OPTIONAL) The name of the resource group.
    --accountName=<val>                     [string]  (OPTIONAL) The name of the Azure Purview account.
    --peopleFile=<val>                      [string]  (OPTIONAL) Path to the document which contains the JSON response from graph.microsoft.com/v1.0/me/people

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
