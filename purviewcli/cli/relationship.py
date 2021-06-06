"""
usage: 
    pv relationship create --payload-file=<val>
    pv relationship put --payload-file=<val>
    pv relationship read --guid=<val> [--extendedInfo]
    pv relationship delete --guid=<val>

options:
    --purviewName=<val>                   [string]  Azure Purview account name.
    --guid=<val>                          [string]  The globally unique identifier of the relationship.
    --extendedInfo                        [boolean] Limits whether includes extended information.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
