"""
usage: 
    pv glossary create --payloadFile=<val>
    pv glossary createCategories --payloadFile=<val>
    pv glossary createCategory --payloadFile=<val>
    pv glossary createTerm --payloadFile=<val> [--includeTermHierarchy]
    pv glossary createTerms --payloadFile=<val> [--includeTermHierarchy]
    pv glossary createTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
    pv glossary createTermsExport --glossaryGuid=<val> --termGuid=<val>... [--includeTermHierarchy]
    pv glossary createTermsImport --glossaryFile=<val> [--glossaryGuid=<val> --includeTermHierarchy]
    pv glossary delete --glossaryGuid=<val>
    pv glossary deleteCategory --categoryGuid=<val>
    pv glossary deleteTerm --termGuid=<val>
    pv glossary deleteTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
    pv glossary put --glossaryGuid=<val> --payloadFile=<val>
    pv glossary putCategory --categoryGuid=<val> --payloadFile=<val>
    pv glossary putCategoryPartial --categoryGuid=<val> --payloadFile=<val>
    pv glossary putPartial --glossaryGuid=<val> --payloadFile=<val> [--includeTermHierarchy]
    pv glossary putTerm --termGuid=<val> --payloadFile=<val> [--includeTermHierarchy]
    pv glossary putTermPartial --termGuid=<val> --payloadFile=<val> [--includeTermHierarchy]
    pv glossary putTermsAssignedEntities --termGuid=<val> --payloadFile=<val>
    pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val> --ignoreTermsAndCategories]
    pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategory --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoryRelated --categoryGuid=<val>
    pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readDetailed --glossaryGuid=<val> [--includeTermHierarchy]
    pv glossary readTerm --termGuid=<val> [--includeTermHierarchy]
    pv glossary readTerms [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val> --extInfo --includeTermHierarchy]
    pv glossary readTermsAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsImport --operationGuid=<val>
    pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]

options:
    --purviewName=<val>         [string]  Azure Purview account name.
    --categoryGuid=<val>        [string]  The globally unique identifier of the category.
    --extInfo                   [boolean] extInfo [defaul: false]
    --glossaryGuid=<val>        [string]  The globally unique identifier for glossary.
    --glossaryName=<val>        [string]  The name of the glossary.
    --includeTermHierarchy      [boolean] Include term template references [default: false].
    --ignoreTermsAndCategories  [boolean] Whether to ignore terms and categories [default: false].
    --limit=<val>               [integer] The page size - by default there is no paging [default: 1000].
    --offset=<val>              [integer] Offset for pagination purpose [default: 0].
    --operationGuid=<val>       [string]  The globally unique identifier for async operation/job.
    --payloadFile=<val>         [string]  File path to a valid JSON document.
    --sort=<val>                [string]  ASC or DESC [default: ASC].
    --termGuid=<val>            [string]  The globally unique identifier for glossary term.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
