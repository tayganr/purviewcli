"""
usage: 
    pv lineage read --guid=<val> [--depth=<val> --width=<val> --direction=<val>]
    pv lineage readNext --guid=<val> [--direction<val> --offset=<val> --limit=<val>]

options:
    --purviewName=<val>               [string]  Azure Purview account name.
    --depth=<depth>                   [integer] The number of hops for lineage [default: 3].
    --width=<width>                   [integer] The number of max expanding width in lineage [default: 6].
    --direction=<direction>           [string]  The direction of the lineage, which could be INPUT, OUTPUT or BOTH [default: BOTH].
    --offset=<val>                    [integer] Offset for pagination purpose [default: 0].
    --limit=<val>                     [integer] The page size - by default there is no paging [default: -1].
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
