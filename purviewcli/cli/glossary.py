"""
usage: 
    pv glossary create --glossaryName=<val>
    pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val>]
    pv glossary update --glossaryGuid=<val> --language=<val>
    pv glossary delete --glossaryGuid=<val>
    pv glossary readDetailed --glossaryGuid=<val>
    pv glossary updatePartial --glossaryGuid=<val> --attrKey=<val>... --attrVal=<val>...
    pv glossary updateCategoryPartial --categoryGuid=<val> --attrKey=<val>... --attrVal=<val>...
    pv glossary updateTermPartial --termGuid=<val> --attrKey=<val>... --attrVal=<val>...
    pv glossary createCategory --glossaryGuid=<val> --categoryName=<val>
    pv glossary readCategory --categoryGuid=<val>
    pv glossary updateCategory --categoryGuid=<val> [--longDescription=<val>]
    pv glossary deleteCategory --categoryGuid=<val>
    pv glossary readCategoryRelated --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary createCategories --glossaryGuid=<val> --categoryName=<val>...
    pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary createTerm --glossaryGuid=<val> --termName=<val> [--status=<val> --longDescription=<val> --abbreviation=<val> --synonym=<val>... --related=<val>... --resourceName=<val>... --resourceUrl=<val>... --expertId=<val>... --stewardId=<val>...]
    pv glossary readTerm --termGuid=<val>
    pv glossary updateTerm --termGuid=<val> [--termName=<val> --glossaryGuid=<val> --status=<val> --longDescription=<val> --abbreviation=<val> --synonym=<val>... --related=<val>... --resourceName=<val>... --resourceUrl=<val>... --expertId=<val>... --stewardId=<val>...]
    pv glossary deleteTerm --termGuid=<val>
    pv glossary createTerms --glossaryGuid=<val> --termName=<val>... [--status=<val>... --longDescription=<val>...]
    pv glossary readTerms --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary createAssignedEntities --termGuid=<val> --guid=<val>...
    pv glossary readAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary deleteAssignedEntities --termGuid=<val> --guid=<val>... --relationshipGuid=<val>...

options:
    --limit=<val>           By default there is no paging [default: -1].
    --offset=<val>          Offset for pagination purpose [default: 0].
    --sort=<val>            ASC or DESC [default: ASC].
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
