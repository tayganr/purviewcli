"""
usage: 
    pv search query [--keywords=<val> --limit=<val> --offset=<val> --filter-file=<val> --facets-file=<val>]

options:
  --purviewName=<val>     [string]  Azure Purview account name.
  --limit=<val>           [integer] By default there is no paging [default: 25].
  --offset=<val>          [integer] Offset for pagination purpose [default: 0].
  --filter-file=<val>     [string]  File path to a filter json file.
  --facets-file=<val>     [string]  File path to a facets json file.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
