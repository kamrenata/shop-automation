import requests
from lib.constants import URL


class HTTPClient:
    def __init__(self):
        self.client = requests
        self.url: str = URL

    def _generate_url(self, route: str): #private protected variable
        return self.url + "/" + route

    def get(self, route, params=None, headers=None, **kwargs):
        if headers is None:
            headers = {"Accept": "application/json"}
        return self.client.get(self._generate_url(route), params=params, headers=headers, **kwargs)

    def post(self, route, data=None, json=None, **kwargs):
        return self.client.post(self._generate_url(route), data=data, json=json, **kwargs)

    def put(self, route, data=None, **kwargs):
        return self.client.put(self._generate_url(route), data=data, **kwargs)

    def delete(self, route, **kwargs):
        return self.client.delete(self._generate_url(route), **kwargs)

