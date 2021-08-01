"""
usage: 
    pv credential delete --credentialName=<val>
    pv credential put --credentialName=<val> --payload-file=<val>
    pv credential read [--credentialName=<val>]

options:
    --purviewName=<val>                   [string]  Azure Purview account name.
    --credentialName=<val>                [string]  The name of the credential.

mapping:
https://{account_name}.proxy.purview.azure.com
+---------+--------+-------------------------------+
| Command | Method | Path                          |
+---------+--------+-------------------------------+
| delete  | DELETE | /credentials/{credentialName} |
| put     | PUT    | /credentials/{credentialName} |
| read    | GET    | /credentials/{credentialName} |
+---------+--------+-------------------------------+


"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)



