from requests.auth import AuthBase
from predictivo_api import exception
import requests


class ClientOauth(AuthBase):

    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'OAuth ' + self.access_token
        return r

    def get_metadata(self):
        try:
            r = requests.get('https://login.predictivo_api.com/oauth2/metadata', auth=self)
            return r.json()
        except requests.exceptions.RequestException as e:
            raise e

    def get_base_url(self):
        url = self.get_metadata()
        if "api_endpoint" in url:
            return url["api_endpoint"]
        else:
            raise exception.InvalidToken("Invalid token unable to load login and user")
