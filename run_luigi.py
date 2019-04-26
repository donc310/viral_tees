import luigi
from datetime import datetime

class QueryTwitterTrends(luigi.ExternalTask):
    import pandas as pd
    from retrieve_trends import run as retrieve_trends

    args_dict = {
        'location': ['usa-nyc']
    }

    date = datetime.now()
    str_date = date.strftime('%m%d_%Y_%H%M')

    def requires(self):
        return []
 
    def output(self):
        return luigi.LocalTarget("data/trends/trends_{}.csv".format(str_date))
 
    def run(self):
        json_data, df_data = retrieve_trends(args_dict)
        df_data.to_csv(self.output())
    
