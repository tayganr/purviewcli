"""
usage: 
    pv relationship create --typeName=<val> --end1Guid=<val> --end1Type=<val> --end2Guid=<val> --end2Type=<val> [--status=<val>]
    pv relationship read --relationshipGuid=<val> [--extendedInfo]
    pv relationship update --relationshipGuid=<val> [--status=<val>]
    pv relationship delete --relationshipGuid=<val>

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
