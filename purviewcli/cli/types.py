"""
usage: 
    pv types createTypedefs --category=<val>... --defName=<val>... [--defDescription=<val>...]
    pv types readTypedefs [--type=<val>]
    pv types updateTypedefs --category=<val>... --defName=<val>... [--defDescription=<val>...]
    pv types deleteTypedefs --defName=<val>...
    pv types readTypedefsHeaders
    pv types readTypedef (--guid=<val> | --name=<val>)
    pv types deleteTypedefName --name=<val>
    pv types readClassificationdef (--guid=<val> | --name=<val>)
    pv types readBusinessmetadatadef (--guid=<val> | --name=<val>)
    pv types readEntitydef (--guid=<val> | --name=<val>)
    pv types readEnumdef (--guid=<val> | --name=<val>)
    pv types readRelationshipdef (--guid=<val> | --name=<val>)
    pv types readStructdef (--guid=<val> | --name=<val>)
    pv types addAttributedef --name=<val> --type=<val> --typeName=<val>

options:
  --type=<val>         Valid Types: classification | entity | enum | relationship | struct
  --category=<val>     Valid Categories: CLASSIFICATION | ENTITY | ENUM | RELATIONSHIP | STRUCT

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
