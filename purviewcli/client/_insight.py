from .endpoint import Endpoint, decorator, get_json
from datetime import datetime, timedelta

class Insight(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'mapanddiscover'

    # Asset
    @decorator
    def insightAssetDistribution(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/serverless/asset2/assetDistribution/getSnapshot'

    @decorator
    def insightFilesWithoutResourceSet(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/serverless/asset2/filesWithoutResourceSet/getSnapshot'

    @decorator
    def insightFilesAggregation(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/serverless/asset2/filesAggregation/getSnapshot'

    @decorator
    def insightTags(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/serverless/asset2/tags/getSnapshot'

    @decorator
    def insightTagsTimeSeries(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/serverless/asset2/tags/timeSeries'

    # Scan
    @decorator
    def insightScanStatusSummary(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/scanstatus2/summaries'
        self.params = { 'window': args['--numberOfDays'] }

    @decorator
    def insightScanStatusSummaryByTs(self, args):
        self.method = 'GET'
        self.endpoint = '/reports/scanstatus2/summariesbyts'
        self.params = { 'window': args['--numberOfDays'] }