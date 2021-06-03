"""
usage: 
    pv relationship create --payload-file=<val>
    pv relationship put --payload-file=<val>
    pv relationship read --guid=<val> [--extendedInfo]
    pv relationship delete --guid=<val>

options:
    --purviewName=<val>                   Azure Purview account name.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
