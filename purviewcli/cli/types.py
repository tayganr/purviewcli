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
    pv types deleteTypeDefs --payload-file=<val>
    pv types createTypeDefs --payload-file=<val>
    pv types putTypeDefs --payload-file=<val>
    pv types readStatistics

options:
  --purviewName=<val>     [string]  Azure Purview account name.
  --type=<val>            [string]  Typedef name as search filter (classification | entity | enum | relationship | struct).
  --includeTermTemplate   [boolean] Whether to include termtemplatedef.
  --guid=<val>            [string]  The globally unique identifier.
  --name=<val>            [string]  The name of the definition.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
