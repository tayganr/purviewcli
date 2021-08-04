"""
usage: 
    pv glossary create --payload-file=<val>
    pv glossary createCategories --payload-file=<val>
    pv glossary createCategory --payload-file=<val>
    pv glossary createTerm --payload-file=<val>
    pv glossary createTerms --payload-file=<val>
    pv glossary createTermsAssignedEntities --termGuid=<val> --payload-file=<val>
    pv glossary createTermsExport --glossaryGuid=<val> --termGuid=<val>...
    pv glossary createTermsImport (--glossaryGuid=<val> | --glossaryName=<val>)
    pv glossary delete --glossaryGuid=<val>
    pv glossary deleteCategory --categoryGuid=<val>
    pv glossary deleteTerm --termGuid=<val>
    pv glossary deleteTermsAssignedEntities --termGuid=<val> --payload-file=<val>
    pv glossary put --glossaryGuid=<val> --payload-file=<val>
    pv glossary putCategory --categoryGuid=<val> --payload-file=<val>
    pv glossary putCategoryPartial --categoryGuid=<val> --payload-file=<val>
    pv glossary putPartial --glossaryGuid=<val> --payload-file=<val>
    pv glossary putTerm --termGuid=<val> --payload-file=<val>
    pv glossary putTermPartial --termGuid=<val> --payload-file=<val>
    pv glossary putTermsAssignedEntities --termGuid=<val> --payload-file=<val>
    pv glossary read [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategories --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoriesHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategory --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readCategoryRelated --categoryGuid=<val>
    pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readDetailed --glossaryGuid=<val>
    pv glossary readTerm --termGuid=<val>
    pv glossary readTerms [--glossaryGuid=<val> --limit=<val> --offset=<val> --sort=<val> --extInfo --includeTermHierarchy]
    pv glossary readTermsAssignedEntities --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsHeaders --glossaryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
    pv glossary readTermsImport --operationGuid=<val>
    pv glossary readTermsRelated --termGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]

options:
    --purviewName=<val>     [string]  Azure Purview account name.
    --categoryGuid=<val>    [string]  The globally unique identifier of the category.
    --extInfo               [boolean] extInfo [defaul: false]
    --glossaryGuid=<val>    [string]  The globally unique identifier for glossary.
    --glossaryName=<val>    [string]  The name of the glossary.
    --includeTermHierarchy  [boolean] Include term template references [default: false]
    --limit=<val>           [integer] The page size - by default there is no paging [default: 1000].
    --offset=<val>          [integer] Offset for pagination purpose [default: 0].
    --operationGuid=<val>   [string]  The globally unique identifier for async operation/job.
    --payload-file=<val>    [string]  File path to a valid JSON document.
    --sort=<val>            [string]  ASC or DESC [default: ASC].
    --termGuid=<val>        [string]  The globally unique identifier for glossary term.

mapping:
https://{account_name}.catalog.purview.azure.com
+-----------------------------+--------+----------------------------------------------------------+
| Command                     | Method | Path                                                     |
+-----------------------------+--------+----------------------------------------------------------+
| create                      | POST   | /api/atlas/v2/glossary                                   |
| createCategories            | POST   | /api/atlas/v2/glossary/categories                        |
| createCategory              | POST   | /api/atlas/v2/glossary/category                          |
| createTerm                  | POST   | /api/atlas/v2/glossary/term                              |
| createTerms                 | POST   | /api/atlas/v2/glossary/terms                             |
| createTermsAssignedEntities | POST   | /api/atlas/v2/glossary/terms/{termGuid}/assignedEntities |
| createTermsExport           | POST   | /api/atlas/v2/glossary/{glossaryGuid}/terms/export       |
| createTermsImport           | POST   | /api/atlas/v2/glossary/{glossaryGuid}/terms/import       |
| delete                      | DELETE | /api/atlas/v2/glossary/{glossaryGuid}                    |
| deleteCategory              | DELETE | /api/atlas/v2/glossary/category/{categoryGuid}           |
| deleteTerm                  | DELETE | /api/atlas/v2/glossary/term/{termGuid}                   |
| deleteTermsAssignedEntities | DELETE | /api/atlas/v2/glossary/terms/{termGuid}/assignedEntities |
| put                         | PUT    | /api/atlas/v2/glossary/{glossaryGuid}                    |
| putCategory                 | PUT    | /api/atlas/v2/glossary/category/{categoryGuid}           |
| putCategoryPartial          | PUT    | /api/atlas/v2/glossary/category/{categoryGuid}/partial   |
| putPartial                  | PUT    | /api/atlas/v2/glossary/{glossaryGuid}/partial            |
| putTerm                     | PUT    | /api/atlas/v2/glossary/term/{termGuid}                   |
| putTermPartial              | PUT    | /api/atlas/v2/glossary/term/{termGuid}/partial           |
| putTermsAssignedEntities    | PUT    | /api/atlas/v2/glossary/terms/{termGuid}/assignedEntities |
| read                        | GET    | /api/atlas/v2/glossary                                   |
| readCategories              | GET    | /api/atlas/v2/glossary/{glossaryGuid}/categories         |
| readCategoriesHeaders       | GET    | /api/atlas/v2/glossary/{glossaryGuid}/categories/headers |
| readCategory                | GET    | /api/atlas/v2/glossary/category/{categoryGuid}           |
| readCategoryRelated         | GET    | /api/atlas/v2/glossary/category/{categoryGuid}/related   |
| readCategoryTerms           | GET    | /api/atlas/v2/glossary/category/{categoryGuid}/terms     |
| readDetailed                | GET    | /api/atlas/v2/glossary/{glossaryGuid}/detailed           |
| readTerm                    | GET    | /api/atlas/v2/glossary/term/{termGuid}                   |
| readTerms                   | GET    | /api/atlas/v2/glossary/{glossaryGuid}/terms              |
| readTermsAssignedEntities   | GET    | /api/atlas/v2/glossary/terms/{termGuid}/assignedEntities |
| readTermsHeaders            | GET    | /api/atlas/v2/glossary/{glossaryGuid}/terms/headers      |
| readTermsImport             | GET    | /api/atlas/v2/glossary/terms/import/{operationGuid}      |
| readTermsRelated            | GET    | /api/atlas/v2/glossary/terms/{termGuid}/related          |
+-----------------------------+---------+---------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
