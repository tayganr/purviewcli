"""
usage: 
    pv lineage read --guid=<val> [--depth=<val> --width=<val> --direction=<val>]
    pv lineage readUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val> [--depth=<val> --direction=<val>]

options:
    --depth=<depth>                   Number of hops for lineage [default: 3].
    --width=<width>                   Custom to Azure Purview [default: 6].
    --direction=<direction>           INPUT or OUTPUT or BOTH [default: BOTH].
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
