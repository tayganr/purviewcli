"""
usage: 
    pv insight assetDistribution
    pv insight filesAggregation
    pv insight filesWithoutResourceSet
    pv insight scanStatusSummary [--numberOfDays=<val>]
    pv insight scanStatusSummaryByTs [--numberOfDays=<val>]
    pv insight tags
    pv insight tagsTimeSeries

options:
    --purviewName=<val>          [string]  Azure Purview account name.
    --numberOfDays=<val>         [integer] Trailing time period in days [default: 30].

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
