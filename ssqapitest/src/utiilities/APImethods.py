from requests_oauthlib import OAuth1
import requests
from ssqapitest.src.utiilities.baseTest import BaseTest
from ssqapitest.src.utiilities.payloads import APIPayloads

class APIMethodsImplementation(object):

    def __init__(self):
        self.endpoint = BaseTest.endpoints
        self.header = BaseTest.header
        self.access_key = BaseTest.auth["access_key"]
        self.access_password = BaseTest.auth["access_password"]
        self.auth = OAuth1(self.access_key,self.access_password)
        self.URI = BaseTest.URI
        self.data = APIPayloads('file')


    def post(self,endpoint=self.endpoint,payloads=self.data,header=self.header,auth=self.auth):

        if not header:
            header = {'content-type':'application/json'}
        url = self.URI + self.endpoint
        response = requests.post(url=url,data=payloads,header=header)

        return response.json()

    def update(self,endpoint=self.endpoint,payloads="",header=self.header,auth=self.auth):
        pass

    def delete(self):
        pass

    def get(self):
        pass
