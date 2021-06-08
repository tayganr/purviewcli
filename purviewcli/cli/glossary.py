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
    pv glossary createTermsExport --glossaryGuid=<val> --termGuid=<val>...
    pv glossary createTermsImport (--glossaryGuid=<val> | --glossaryName=<val>)
    pv glossary readTerms --glossaryName=<val>
    pv glossary readTermsImport --operationGuid=<val>

options:
    --purviewName=<val>     [string]  Azure Purview account name.
    --glossaryGuid=<val>    [string]  The globally unique identifier for glossary.
    --categoryGuid=<val>    [string]  The globally unique identifier of the category.
    --termGuid=<val>        [string]  The globally unique identifier for glossary term.
    --operationGuid=<val>   [string]  The globally unique identifier for async operation/job.
    --glossaryName=<val>    [string]  The name of the glossary.
    --limit=<val>           [integer] The page size - by default there is no paging [default: -1].
    --offset=<val>          [integer] Offset for pagination purpose [default: 0].
    --sort=<val>            [string]  ASC or DESC [default: ASC].
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
