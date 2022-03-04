"""
usage: 
    pv credential delete --credentialName=<val>
    pv credential put --credentialName=<val> --payloadFile=<val>
    pv credential read [--credentialName=<val>]

options:
    --purviewName=<val>                   [string]  Azure Purview account name.
    --credentialName=<val>                [string]  The name of the credential.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)



