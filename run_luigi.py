import luigi
from datetime import datetime

class QueryTwitterTrends(luigi.Task):
    from retrieve_trends import run as retrieve_trends

    args = {
        'country': 1;
    }

    date = datetime.now()
    str_date = date.strftime('%m%d_%Y_%H%M')

    def requires(self):
        return []
 
    def output(self):
        return luigi.LocalTarget("data/trends/trends_{}.csv".format(str_date))
 
    def run(self):
        retrieve_trends(args)
