"""
usage: 
    pv relationship create --payload-file=<val>
    pv relationship delete --guid=<val>
    pv relationship put --payload-file=<val>
    pv relationship read --guid=<val> [--extendedInfo]

options:
    --purviewName=<val>           [string]  Azure Purview account name.
    --extendedInfo                [boolean] Limits whether includes extended information [default: false].
    --guid=<val>                  [string]  The globally unique identifier of the relationship.
    --payload-file=<val>          [string]  File path to a valid JSON document.

mapping:
https://{account_name}.catalog.purview.azure.com
+---------+--------+----------------------------------------+
| Command | Method | Path                                   |
+---------+--------+----------------------------------------+
| create  | POST   | /api/atlas/v2/relationship             |
| delete  | DELETE | /api/atlas/v2/relationship/guid/{guid} |
| put     | PUT    | /api/atlas/v2/relationship             |
| read    | GET    | /api/atlas/v2/relationship/guid/{guid} |
+---------+--------+----------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
