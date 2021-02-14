"""
usage: 
    pv relationship create <typeName> <status> <end1Guid> <end2Guid>
    pv relationship read <guid> [--extendedInfo]
    pv relationship update <guid> [--status=<val> --end1Guid=<val> --end2Guid=<val>]
    pv relationship delete <guid> 

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
