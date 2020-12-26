class APIMethodsImplementation(object):
from ssqapitest.src.utiilities.baseTest import BaseTest
    def __init__(self):
        self.endpoint = BaseTest.endpoints
        self.header = BaseTest.header
        self.access_key = BaseTest.auth["access_key"]
        self.access_password = BaseTest.auth["access_password"]


    def post(self,endpoint,payloads,header,auth):
        pass

    def update(self,endpoint=self.endpoint,payloads="",header=self.header,auth=self.auth):

    def delete(self):
        pass

    def get(self):
        pass
