"""
usage: 
    pv lineage read --guid=<val> [--depth=<val> --width=<val> --direction=<val>]
    pv lineage readNext --guid=<val> [--direction<val> --offset=<val> --limit=<val>]

options:
    --purviewName=<val>               [string]  Azure Purview account name.
    --depth=<depth>                   [integer] The number of hops for lineage [default: 3].
    --direction=<direction>           [string]  The direction of the lineage, which could be INPUT, OUTPUT or BOTH [default: BOTH].
    --guid=<val>                      [string]  The globally unique identifier of the entity.
    --limit=<val>                     [integer] The page size - by default there is no paging [default: -1].
    --offset=<val>                    [integer] Offset for pagination purpose [default: 0].
    --width=<width>                   [integer] The number of max expanding width in lineage [default: 6].

mapping:
https://{account_name}.catalog.purview.azure.com
+----------+--------+------------------------------------+
| Command  | Method | Path                               |
+----------+--------+------------------------------------+
| read     | GET    | /api/atlas/v2/lineage/{guid}       |
| readNext | GET    | /api/atlas/v2/lineage/{guid}/next/ |
+----------+--------+------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
