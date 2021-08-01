"""
usage: 
    pv types createTypeDefs --payload-file=<val>
    pv types deleteTypeDef --name=<val>
    pv types deleteTypeDefs --payload-file=<val>
    pv types putTypeDefs --payload-file=<val>
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
  --payload-file=<val>    [string]  File path to a valid JSON document.
  --type=<val>            [string]  Typedef name as search filter (classification | entity | enum | relationship | struct).

mapping:
https://{account_name}.catalog.purview.azure.com
+-----------------------+--------+-----------------------------------------------------------------+
| Command               | Method | Path                                                            |
+-----------------------+--------+-----------------------------------------------------------------+
| createTypeDefs        | POST   | /api/atlas/v2/types/typedefs                                    |
| deleteTypeDef         | DELETE | /api/atlas/v2/types/typedef/name/{name}                         |
| deleteTypeDefs        | DELETE | /api/atlas/v2/types/typedefs                                    |
| putTypeDefs           | PUT    | /api/atlas/v2/types/typedefs                                    |
| readClassificationDef | GET    | /api/atlas/v2/types/classificationdef/{typeDefKey}/{typeDefVal} |
| readEntityDef         | GET    | /api/atlas/v2/types/entitydef/{typeDefKey}/{typeDefVal}         |
| readEnumDef           | GET    | /api/atlas/v2/types/enumdef/{typeDefKey}/{typeDefVal}           |
| readRelationshipDef   | GET    | /api/atlas/v2/types/relationshipdef/{typeDefKey}/{typeDefVal}   |
| readStatistics        | GET    | /api/atlas/v2/types/statistics                                  |
| readStructDef         | GET    | /api/atlas/v2/types/structdef/{typeDefKey}/{typeDefVal}         |
| readTermTemplateDef   | GET    | /api/atlas/v2/types/termtemplatedef/{typeDefKey}/{typeDefVal}   |
| readTypeDef           | GET    | /api/atlas/v2/types/typedef/{typeDefKey}/{typeDefVal}           |
| readTypeDefs          | GET    | /api/atlas/v2/types/typedefs                                    |
| readTypeDefsHeaders   | GET    | /api/atlas/v2/types/typedefs/headers                            |
+-----------------------+--------+-----------------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
