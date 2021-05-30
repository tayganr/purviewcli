"""
usage: 
    pv search query [--keywords=<val> --filter-file=<val> --limit=<val> --offset=<val> --facets-file=<val>]

options:
  --purviewName=<val>   Azure Purview account name.
  --limit=<val>         By default there is no paging [default: 25].
  --offset=<val>        Offset for pagination purpose [default: 0].
  --filter-file=<val>   File path to a filter json file.
  --facets-file=<val>   File path to a facets json file.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
