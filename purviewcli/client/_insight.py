from .endpoint import Endpoint, decorator, get_json
from datetime import datetime, timedelta

class Insight(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'insight'

    @decorator
    def insightGraphql(self, args):
        self.app = 'guardian'
        self.method = 'POST'
        self.endpoint = '/graphql'
        self.payload = get_json(args,'--payload-file')

    @decorator
    def insightFileExtensions(self, args):
        self.app = 'guardian'
        self.method = 'POST'
        self.endpoint = '/reports/fileExtensions'
        startDateTime = (datetime.now() - timedelta(days=int(args['--numberOfDays']))).strftime('%Y-%m-%dT%H:%M:00.000Z')
        endDateTime = datetime.now().strftime('%Y-%m-%dT%H:%M:00.000Z')
        self.payload = {
            "Query":{
                "StartTime": startDateTime,
                "EndTime": endDateTime,
                "takeTopCount": args['--takeTopCount'],
                "assetTypes":[]
            }
        }

    @decorator
    def insightAssetDistribution(self, args):
        self.method = 'GET'
        self.endpoint = '/mapanddiscover/reports/asset2/assetDistribution/getSnapshot'

    @decorator
    def insightAssetDataSources(self, args):
        self.method = 'POST'
        self.endpoint = '/mapanddiscover/reports/asset2/dataSources'
        self.payload = {"registeredSourceGroup":""}

    @decorator
    def insightFilesWithoutResourceSet(self, args):
        self.method = 'GET'
        self.endpoint = '/mapanddiscover/reports/asset2/filesWithoutResourceSet/getSnapshot'

    @decorator
    def insightFileTypeSizeTimeSeries(self, args):
        self.method = 'POST'
        self.endpoint = '/mapanddiscover/reports/asset2/fileTypeSizeTimeSeries'
        self.payload = {
            "window": f"{args['--numberOfDays']}d",
            "fileType": args['--fileType'],
            "dataSource": args['--dataSource'],
            "registeredSourceGroup":""
        }

    @decorator
    def insightTopFileTypesBySize(self, args):
        self.method = 'POST'
        self.endpoint = '/mapanddiscover/reports/asset2/topFileTypesBySize'
        self.payload = {"dataSource":"","registeredSourceGroup":""}

    @decorator
    def insightScanStatusSummaries(self, args):
        self.method = 'GET'
        self.endpoint = '/mapanddiscover/reports/scanstatus2/summaries'
        self.params = { 'window': args['--numberOfDays'] }

    @decorator
    def insightScanStatusSummariesByTs(self, args):
        self.method = 'GET'
        self.endpoint = '/mapanddiscover/reports/scanstatus2/summariesbyts'
        self.params = { 'window': args['--numberOfDays'] }