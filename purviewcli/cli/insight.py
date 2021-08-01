"""
usage: 
    pv insight assetDataSources
    pv insight assetDistribution
    pv insight fileExtensions [--numberOfDays=<val> --takeTopCount=<val>]
    pv insight fileTypeSizeTimeSeries [--numberOfDays=<val> --fileType=<val> --dataSource=<val>]
    pv insight filesWithoutResourceSet
    pv insight graphql --payload-file=<val>
    pv insight scanStatusSummaries [--numberOfDays=<val>]
    pv insight scanStatusSummariesByTs [--numberOfDays=<val>]
    pv insight topFileTypesBySize

options:
    --purviewName=<val>               Azure Purview account name.
    --numberOfDays=<val>              Trailing time period in days [default: 30].
    --takeTopCount=<val>              Specify the maximum number of records to return [default: 10].
    --fileType=<val>                  Specify a file type (csv | avro | parquet | json | snappy | pptx | docx | xlsx) [default: csv].
    --dataSource=<val>                Specify a data source (Azure Blob Storage | aws | Azure Data Lake Storage Gen2).


command to api mapping:
+-------------------------+--------+--------------------------------------------------------------------+
| Command                 | Method | Endpoint                                                           |
+-------------------------+--------+--------------------------------------------------------------------+
| assetDataSources        | POST   | /mapanddiscover/reports/asset2/dataSources                         |                                      
| assetDistribution       | GET    | /mapanddiscover/reports/asset2/assetDistribution/getSnapshot       |                                                      
| fileExtensions          | POST   | /reports/fileExtensions                                            |                  
| fileTypeSizeTimeSeries  | POST   | /mapanddiscover/reports/asset2/fileTypeSizeTimeSeries              |                                                  
| filesWithoutResourceSet | GET    | /mapanddiscover/reports/asset2/filesWithoutResourceSet/getSnapshot |                                                              
| graphql                 | POST   | /graphql                                                           |  
| scanStatusSummaries     | GET    | /mapanddiscover/reports/scanstatus2/summaries                      |                                          
| scanStatusSummariesByTs | GET    | /mapanddiscover/reports/scanstatus2/summariesbyts                  |    
| topFileTypesBySize      | POST   | /mapanddiscover/reports/asset2/topFileTypesBySize                  |                                              
+-------------------------+--------+--------------------------------------------------------------------+                                          

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
