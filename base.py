import os
import requests
import base64

BASE_URL = 'https://api.twitter.com'
API_EP = '{}/oauth2/token'.format(BASE_URL)

class Twitter(object):

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def request(self):
        auth = '{}:{}'.format(self.key, self.secret).encode('ascii')
        b64_encoded_key = base64.b64encode(auth)
        b64_encoded_key = b64_encoded_key.decode('ascii')

        import pdb; pdb.set_trace()

        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        self.auth_resp = requests.post(API_EP, headers=auth_headers, data=auth_data)

        return self.auth_resp