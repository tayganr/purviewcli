"""
usage: 
    pv demo generate --subscriptionId=<val> --location=<val> [--resourceGroupName=<val> --people-file=<val>]

options:
    --subscriptionId=<val>                  [string]  The subscription ID.
    --resourceGroupName=<val>               [string]  The name of the resource group.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
