"""
usage: 
    pv types readTypedefs [--includeTermTemplate --type=<val>]
    pv types readTypedefsHeaders [--includeTermTemplate --type=<val>]
    pv types readBusinessmetadatadef (--guid=<val> | --name=<val>)
    pv types readClassificationdef (--guid=<val> | --name=<val>)
    pv types readEntitydef (--guid=<val> | --name=<val>)
    pv types readEnumdef (--guid=<val> | --name=<val>)
    pv types readRelationshipdef (--guid=<val> | --name=<val>)
    pv types readStructdef (--guid=<val> | --name=<val>)
    pv types readTypedef (--guid=<val> | --name=<val>)
    pv types deleteTypedef --name=<val>
    pv types deleteTypedefs --payload-file
    pv types createTypedefs --payload-file
    pv types putTypedefs --payload-file

options:
  --purviewName=<val>    Azure Purview account name.
  --type=<val>           Valid Types: classification | entity | enum | relationship | struct.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
