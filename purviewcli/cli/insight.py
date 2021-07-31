"""
usage: 
    pv insight graphql --payload-file=<val>
    pv insight fileExtensions [--numberOfDays=<val> --takeTopCount=<val>]
    pv insight assetDistribution
    pv insight assetDataSources
    pv insight filesWithoutResourceSet
    pv insight fileTypeSizeTimeSeries [--numberOfDays=<val> --fileType=<val> --dataSource=<val>]
    pv insight topFileTypesBySize
    pv insight scanStatusSummaries [--numberOfDays=<val>]
    pv insight scanStatusSummariesByTs [--numberOfDays=<val>]

options:
    --purviewName=<val>               Azure Purview account name.
    --numberOfDays=<val>              Trailing time period in days [default: 30].
    --takeTopCount=<val>              Specify the maximum number of records to return [default: 10].
    --fileType=<val>                  Specify a file type (csv | avro | parquet | json | snappy | pptx | docx | xlsx) [default: csv].
    --dataSource=<val>                Specify a data source (Azure Blob Storage | aws | Azure Data Lake Storage Gen2).

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
