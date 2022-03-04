"""
usage: 
    pv insight assetDataSources
    pv insight assetDistribution
    pv insight fileExtensions [--numberOfDays=<val> --takeTopCount=<val>]
    pv insight fileTypeSizeTimeSeries [--numberOfDays=<val> --fileType=<val> --dataSource=<val>]
    pv insight filesWithoutResourceSet
    pv insight graphql --payloadFile=<val>
    pv insight scanStatusSummaries [--numberOfDays=<val>]
    pv insight scanStatusSummariesByTs [--numberOfDays=<val>]
    pv insight topFileTypesBySize

options:
    --purviewName=<val>          [string]  Azure Purview account name.
    --dataSource=<val>           [string]  Specify a data source (Azure Blob Storage | aws | Azure Data Lake Storage Gen2).
    --fileType=<val>             [string]  Specify a file type (csv | avro | parquet | json | snappy | pptx | docx | xlsx) [default: csv].
    --numberOfDays=<val>         [integer] Trailing time period in days [default: 30].
    --payloadFile=<val>          [string]  File path to a valid JSON document.
    --takeTopCount=<val>         [integer] Specify the maximum number of records to return [default: 10].

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
