"""
usage: 
    pv typedefs read [--type=<val>]
    pv typedefs readHeaders
    pv typedefs deleteTypedefName --name=<val>
    pv typedefs createClassificationdefs --defName=<val>... [--defDescription=<val>... --defDisplayName=<val>...]
    pv typedefs readClassificationdef (--guid=<val> | --name=<val>)
    pv typedefs updateClassificationdefs --defName=<val>... [--defDescription=<val>... --defDisplayName=<val>...]
    pv typedefs deleteClassificationdef (--guid=<val> | --name=<val>)
    pv typedefs readBusinessmetadatadef (--guid=<val> | --name=<val>)
    pv typedefs readEntitydef (--guid=<val> | --name=<val>)
    pv typedefs readEnumdef (--guid=<val> | --name=<val>)
    pv typedefs readRelationshipdef (--guid=<val> | --name=<val>)
    pv typedefs readStructdef (--guid=<val> | --name=<val>)
    pv typedefs readTypedef (--guid=<val> | --name=<val>)

options:
  --type=<val>         Definition Type: classification | entity | enum | relationship | struct.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
