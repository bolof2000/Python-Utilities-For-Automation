from requests_oauthlib import OAuth1
from ssqapitest.src.utiilities.baseTest import BaseTest
class APIMethodsImplementation(object):

    def __init__(self):
        self.endpoint = BaseTest.endpoints
        self.header = BaseTest.header
        self.access_key = BaseTest.auth["access_key"]
        self.access_password = BaseTest.auth["access_password"]
        self.auth = OAuth1(self.access_key,self.access_password)


    def post(self,endpoint=self.endpoint,payloads="",header=self.header,auth=self.auth):
        pass

    def update(self,endpoint=self.endpoint,payloads="",header=self.header,auth=self.auth):
        pass

    def delete(self):
        pass

    def get(self):
        pass
