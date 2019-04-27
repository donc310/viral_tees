import luigi
import pickle
from datetime import datetime


class QueryTwitterTrends(luigi.ExternalTask):

    def requires(self):
        return []

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

    def output(self, **kwargs):
        date = datetime.now()
        str_date = date.strftime('%m%d_%Y_%H%M')

        return luigi.LocalTarget(
            "data/trends/trends_{}_{}.csv".format(str_date, kwargs['loc']))


class EmailTwitterTrends(luigi.ExternalTask):

    def requires(self):
        return [QueryTwitterTrends()]

    def output(self):
        date = datetime.now()
        str_date = date.strftime('%m%d_%Y_%H%M')

        return luigi.LocalTarget("data/trends/trends_{}.pickle".format(str_date))

    def run(self):
        from send_email import run as execute, send_message
        
        args_dict = {
            {'authentication': ['token.pickle'], 'receivers': ['mitchbregs@gmail.com'], 'attachments': self.input()}
        }

        auth, sender, msg = execute(args_dict)

        send_message(auth, sender, msg)

        f = self.output().open('w')
        pickle.dump((auth, sender, msg), f)
        f.close()


if __name__ == '__main__':
    luigi.run()
