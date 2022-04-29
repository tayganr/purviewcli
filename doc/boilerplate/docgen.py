import csv
import os

from pkg_resources import require

def getRequiredArgs(args):
    required_args = args.split('[')[0].replace('(','').replace(')','').replace(' --','--')
    required_args = required_args.split('--')
    required_args = list(filter(None, required_args))
    return required_args

def getOptionalArgs(args):
    optional_args = None
    if len(args.split('[')) > 1:
        optional_args = args.split('[')[1].replace(']','').replace(' --','--')
        optional_args = optional_args.split('--')
        optional_args = list(filter(None, optional_args))
    return optional_args

with open('./doc/boilerplate/boilerplate.csv') as file:
    reader = csv.reader(file, delimiter=',',quotechar='"')
    next(reader, None)
    for row in reader:
        # Get values from CSV
        h1 = row[0]
        h2 = row[1]
        h3 = row[2]
        syntax = row[3]
        description = row[4]
        doc_link = row[5]
        http_method = row[6]
        endpoint = row[7]
        split_syntax = syntax.split(' ')
        cmd = split_syntax[1]
        action = split_syntax[2]

        # Arguments
        markdown_required_args = ''
        markdown_optional_args = ''
        if len(split_syntax) > 3:
            offset = len(cmd) + len(action) + 5
            args = syntax[offset:]
            required_args = getRequiredArgs(args)
            optional_args = getOptionalArgs(args)

            # Gen Required Args Markdown
            if required_args is not None:
                for arg in required_args:
                    arg_name = arg.split('=<val>')[0]
                    markdown_required_args += f"`--{arg_name}` (string)  \nDESC.\n\n"
                markdown_required_args = markdown_required_args[:-2]
            else:
                markdown_required_args = f"*None*"

            # Gen Optional Args Markdown
            if optional_args is not None:
                for arg in optional_args:
                    arg_name = arg.split('=<val>')[0]
                    markdown_optional_args += f"`--{arg_name}` (string)  \nDESC.\n\n"
                markdown_optional_args = markdown_optional_args[:-2]
            else:
                markdown_optional_args = f"*None*"
        else:
            pass
        
        # Template
        with open('./doc/boilerplate/template.md', 'r') as file:
            filedata = file.read()
        
        filedata = filedata.replace('{{COMMAND}}',cmd)
        filedata = filedata.replace('{{ACTION}}',action)
        filedata = filedata.replace('{{DESCRIPTION}}',description)
        filedata = filedata.replace('{{SYNTAX}}',syntax)
        filedata = filedata.replace('{{REQUIRED_ARGS}}',markdown_required_args)
        filedata = filedata.replace('{{OPTIONAL_ARGS}}',markdown_optional_args)
        filedata = filedata.replace('{{H1}}',h1)
        filedata = filedata.replace('{{H2}}',h2)
        filedata = filedata.replace('{{H3}}',h3)
        filedata = filedata.replace('{{DOC_LINK}}',doc_link)
        filedata = filedata.replace('{{METHOD}}',http_method)
        filedata = filedata.replace('{{ENDPOINT}}',endpoint)

        filepath = f"./doc/boilerplate/temp/{cmd}" 
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        with open(f"{filepath}/{action}.md", 'w') as file:
            file.write(filedata)

