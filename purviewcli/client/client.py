import logging
import json
import requests
from azure.identity import DefaultAzureCredential

logging.getLogger("azure.identity").setLevel(logging.ERROR)

class PurviewClient():
    def __init__(self, account_name):
        self.access_token = None
        self.account_name = account_name

    def set_token(self):
        credential = DefaultAzureCredential()
        token = credential.get_token('https://purview.azure.net/.default')
        self.access_token = token.token

    def get_token(self):
        return self.access_token

    def http_get(self, app, method, endpoint, params, payload):
        uri = 'https://%s.%s.purview.azure.com%s' % (self.account_name, app, endpoint)
        headers = {"Authorization": "Bearer {0}".format(self.access_token)}
        response = requests.request(method, uri, params=params, json=payload, headers=headers)
        status_code = response.status_code
        if status_code == 204:
            data = {
                'operation': '[%s] %s' % (method, response.url),
                'status': 'The server successfully processed the request'
            }
        else:
            try:
                data = response.json()
            except ValueError:
                data = {
                    'url': response.url,
                    'status_code': response.status_code,
                    'reason': response.reason
                }
        return data

    from ._glossary import (
        getGlossary,
        createGlossary,
        createGlossaryCategory,
        createGlossaryCategories,
        getGlossaryTemplate,
        getGlossaryCategories,
        getGlossaryCategoriesHeaders,
        getGlossaryCategory,
        getGlossaryCategoryRelated,
        getGlossaryCategoryTerms,
        getGlossaryDetailed,
        getGlossaryTerm,
        getGlossaryTerms,
        getAssignedEntities,
        assignEntities,
        getGlossaryTermsHeaders,
        getGlossaryTermsRelated,
        deleteGlossaryTerm,
        purgeGlossaryTerms,
        deleteGlossary,
        deleteGlossaryCategory,
        deleteAssignedEntities,
        createGlossaryTerm,
        createGlossaryTerms,
        updateGlossaryTerm
    )
    from ._entity import (
        assignLabels,
        getEntityAudit,
        getEntityBulk,
        deleteEntityBulk,
        getEntityBulkHeaders,
        getEntityBulkUniqueAttributeType,
        getEntityBusinessmetadataImportTemplate,
        getEntity,
        createEntity,
        createEntityBulk,
        deleteEntity,
        addEntityClassifications,
        getEntityClassification,
        deleteEntityClassification,
        getEntityClassifications,
        getEntityHeader,
        getEntityUniqueAttributeType,
        getEntityUniqueAttributeTypeHeader
    )
    from ._guardian import (
        getAssetDistributionByDataSource,
        getAssetDistributionByTopPaths,
        getFileTypeSizeTimeSeries,
        getFileTypeSizeTrendByDataSource,
        getRegisteredSourceGroupsWithAssets,
        getTopFileTypesBySize,
        getTopLevelSummary
    )
    from ._lineage import (
        getLineage,
        getLineageUniqueAttributeType
    )
    from ._relationship import (
        getRelationship,
        deleteRelationship,
        createRelationship,
        updateRelationship
    )
    from ._scan import (
        getDatasource,
        getDatasources,
        getScan,
        getScanFilters,
        getScanHistory,
        getScanRulesets,
        getScans,
        getSystemScanRulesets,
        getSystemScanRulesetsSettings,
        runScan,
        getClassificationRules,
        getClassificationRule
    )
    from ._search import (
        search
    )
    from ._typedefs import (
        getBusinessmetadatadef,
        getClassificationdef,
        deleteClassificationdef,
        createClassificationdefs,
        updateClassificationdefs,
        getEntitydef,
        getEnumdef,
        getRelationshipdef,
        getStructdef,
        getTypedef,
        deleteTypedefName,
        getTypedefs,
        getTypedefsHeaders
    )