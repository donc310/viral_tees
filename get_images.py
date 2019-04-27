import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_tweets_with_images(url_list):
    for url in url_list:
        d = requests.get(url).text
        soup = BeautifulSoup(d, 'html.parser')

        result_set = soup.find_all('a', href=lambda href: href and "images" in href)
        left = (str(result_set).split('href="', 1)[1])
        photo_link = left[:left.find('"')]

        photos_url = 'twitter.com{}'.format(photo_link)
        print(photos_url)


def get_trend_csv(link):
    trends = pd.read_csv(link)
    url_list = trends['url'].tolist()
    get_tweets_with_images(url_list)

if __name__ == '__main__':
    link = 'csvs/trends_0425_2019_2323_usa-sfo.csv'
    get_trend_csv(link)