from base import Twitter
import os
from dotenv import load_dotenv
load_dotenv('.env')

key = os.getenv('TWITTER_API_KEY')
secret = os.getenv('TWITTER_API_SECRET')

import pdb; pdb.set_trace()

tw = Twitter(key, secret)

response = tw.request()

import pdb; pdb.set_trace()