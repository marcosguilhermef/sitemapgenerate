import requests
from dotenv import dotenv_values

config = dotenv_values(".env")


class Request:
    def __init__(self, url, data, header=None):
        self.url = url
        self.header = header
        self.data = data

    def make_request(self):
        if self.data:
            self.request = requests.get(self.url, data=self.data)
        else:
            self.request = requests.get(self.url)
        return self

    def make_request_post(self):
        if self.data:
            self.request = requests.post(self.url, data=self.data)
        else:
            self.request = requests.post(self.url)
        return self

    def getResponse(self):
        return self.request
