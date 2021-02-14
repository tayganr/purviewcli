"""
usage: 
    pv search advanced [--keywords=<val> --limit=<val> --offset=<val> --facet=<val>...]

options:
  --limit=<val>         By default there is no paging [default: -1].
  --offset=<val>        Offset for pagination purpose [default: 0].
  --facet=<val>         Values: assetType | classification | contactId | label | term | classificationCategory | fileExtension.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
