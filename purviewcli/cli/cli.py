
"""
usage: pv [--version] [--help] <command> [<args>...]

options:
   -v, --version
   -h, --help
   

The most commonly used pv commands are:
   pv entity           [Atlas] Entities are a collection of attributes that model or represent an asset.
   pv glossary         [Atlas] Vocabularies for business users.
   pv lineage          [Atlas] Helps you understand the source and impact of data and changes to data over time.
   pv relationship     [Atlas] Relationships describe connections between two entities.
   pv types            [Atlas] A Type in Atlas is a definition of how a particular object type is stored and accessed.
   pv scan             [Other] Azure Purview scan.
   pv insight          [Other] Azure Purview insights.
   pv search           [Other] Azure Purview advanced search.

See 'pv <command>' for more information on a specific command.

"""
import sys
import json
import importlib
from docopt import docopt
from purviewcli import __version__

def main():
    if len(sys.argv) == 1:
        sys.argv.append('-h')
        sys.exit(main())
    args = docopt(__doc__, version=__version__, options_first=True)
    argv = [args['<command>']] + args['<args>']

    # Command
    command = args['<command>']
    if command in ['entity', 'relationship', 'lineage', 'glossary', 'types', 'scan', 'insight', 'search']:
        globals()[command] = importlib.import_module('purviewcli.cli.' + command)
        command_args = docopt(eval(command).__doc__, argv=argv)
    else:
        exit("%r is not a purviewcli command." % args['<command>'])

    # Action
    action = None
    for item in command_args:
        if item[0] != '-' and item[0] != '<' and item != command and command_args[item] is True:
            action = item
    globals()['lib'] = importlib.import_module('purviewcli.client._' + command)

    # Method
    funcStr = command + action[0].upper() + action[1:]
    funcObj = eval('lib.' + funcStr)
    data = funcObj(command_args)
    
    # Print data
    if len(data) > 0:
        print(json.dumps(data, indent=4, sort_keys=True)) 
    else:
        print('[INFO] No data found for %s.' % (command))

if __name__ == '__main__':
    main()
