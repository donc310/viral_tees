import luigi
from datetime import datetime

class QueryTwitterTrends(luigi.Task):

    def requires(self):
        return []
 
    def output(self, **kwargs):
        date = datetime.now()
        str_date = date.strftime('%m%d_%Y_%H%M')
        kwargs.setdefault('loc', '?')

        return luigi.LocalTarget("data/trends/trends_{}_{}.csv".format(kwargs['loc'], str_date))
 
    def run(self):
        from retrieve_trends import run as retrieve_trends
        import pandas as pd

        locations = [
                'usa-nyc', 
                'usa-lax', 
                'usa-chi', 
                'usa-dal',
                'usa-hou',
                'usa-wdc',
                'usa-mia',
                'usa-phi',
                'usa-atl',
                'usa-bos',
                'usa-phx',
                'usa-sfo',
                'usa-det',
                'usa-sea',
        ]

        for loc in locations:
            args_dict = {
                'location': [loc]
            }

            json_data, df_data = retrieve_trends(args_dict)
            f = self.output(loc=loc).open('w')
            df_data.to_csv(f, sep=',', encoding='utf-8')
            f.close()
   
if __name__ == '__main__':
    luigi.run()
