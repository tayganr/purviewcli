"""
usage: 
    pv types readTypeDefs [--includeTermTemplate --type=<val>]
    pv types readTypeDefsHeaders [--includeTermTemplate --type=<val>]
    pv types readTermTemplateDef (--guid=<val> | --name=<val>)
    pv types readClassificationDef (--guid=<val> | --name=<val>)
    pv types readEntityDef (--guid=<val> | --name=<val>)
    pv types readEnumDef (--guid=<val> | --name=<val>)
    pv types readRelationshipDef (--guid=<val> | --name=<val>)
    pv types readStructDef (--guid=<val> | --name=<val>)
    pv types readTypeDef (--guid=<val> | --name=<val>)
    pv types deleteTypeDef --name=<val>
    pv types deleteTypeDefs --payload-file
    pv types createTypeDefs --payload-file
    pv types putTypeDefs --payload-file
    pv types readStatistics

options:
  --purviewName=<val>    Azure Purview account name.
  --type=<val>           Valid Types: classification | entity | enum | relationship | struct.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
