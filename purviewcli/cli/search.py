"""
usage: 
    pv search query [--keywords=<val> --filter=<val> --limit=<val> --offset=<val> --facets=<val>...]

options:
  --filter=<val>        Filter JSON payload (dictionary).
  --limit=<val>         By default there is no paging [default: 25].
  --offset=<val>        Offset for pagination purpose [default: 0].
  --facets=<val>        Facets JSON payload (array).

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
