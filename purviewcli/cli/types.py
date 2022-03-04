"""
usage: 
    pv types createTypeDefs --payloadFile=<val>
    pv types deleteTypeDef --name=<val>
    pv types deleteTypeDefs --payloadFile=<val>
    pv types putTypeDefs --payloadFile=<val>
    pv types readClassificationDef (--guid=<val> | --name=<val>)
    pv types readEntityDef (--guid=<val> | --name=<val>)
    pv types readEnumDef (--guid=<val> | --name=<val>)
    pv types readRelationshipDef (--guid=<val> | --name=<val>)
    pv types readStatistics
    pv types readStructDef (--guid=<val> | --name=<val>)
    pv types readTermTemplateDef (--guid=<val> | --name=<val>)
    pv types readTypeDef (--guid=<val> | --name=<val>)
    pv types readTypeDefs [--includeTermTemplate --type=<val>]
    pv types readTypeDefsHeaders [--includeTermTemplate --type=<val>]

options:
  --purviewName=<val>     [string]  Azure Purview account name.
  --guid=<val>            [string]  The globally unique identifier.
  --includeTermTemplate   [boolean] Whether to include termtemplatedef [default: false].
  --name=<val>            [string]  The name of the definition.
  --payloadFile=<val>     [string]  File path to a valid JSON document.
  --type=<val>            [string]  Typedef name as search filter (classification | entity | enum | relationship | struct).

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
