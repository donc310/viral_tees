import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup
import urllib3
import re

def get_tweets_with_images(url_list):
    for url in url_list:
        d = requests.get(url).text
        soup = BeautifulSoup(d, 'html.parser')

        meta_data = soup.find_all('a', href=lambda href: href and "images" in href)
        print(type(meta_data))
        break


def get_trend_csv(link):
    trends = pd.read_csv(link)
    url_list = trends['url'].tolist()
    get_tweets_with_images(url_list)

if __name__ == '__main__':
    link = 'csvs/trends_0425_2019_2323_usa-sfo.csv'
    get_trend_csv(link)