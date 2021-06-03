"""
usage: 
    pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val>]
    pv glossary create --payload-file=<val>
    pv glossary createCategories --payload-file=<val>
    pv glossary createCategory --payload-file=<val>
    pv glossary deleteCategory --categoryGuid=<val>
    pv glossary readCategory --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary putCategory --categoryGuid=<val> --payload-file=<val>
    pv glossary putCategoryPartial --categoryGuid=<val> --payload-file=<val>
    pv glossary readCategoryRelated --categoryGuid=<val>
    pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary createTemplate --payload-file=<val>
    pv glossary readTemplate
    pv glossary createTerm --payload-file=<val>
    pv glossary deleteTerm --termGuid=<val>
    pv glossary readTerm --termGuid=<val>
    pv glossary putTerm --termGuid=<val> --payload-file=<val>
    pv glossary putTermPartial --termGuid=<val> --payload-file=<val>
    pv glossary createTerms --payload-file=<val>
    pv glossary deleteTermsAssignedEntities --termGuid=<val> --payload-file=<val>
    pv glossary readTermsAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary createTermsAssignedEntities --termGuid=<val> --payload-file=<val>
    pv glossary putTermsAssignedEntities --termGuid=<val> --payload-file=<val>
    pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary delete --glossaryGuid=<val>
    pv glossary put --glossaryGuid=<val> --payload-file=<val>
    pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readDetailed --glossaryGuid=<val>
    pv glossary putPartial --glossaryGuid=<val> --payload-file=<val>
    pv glossary readTerms --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]

options:
    --purviewName=<val>     Azure Purview account name.
    --limit=<val>           By default there is no paging [default: -1].
    --offset=<val>          Offset for pagination purpose [default: 0].
    --sort=<val>            ASC or DESC [default: ASC].
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
