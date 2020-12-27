from ssqapitest.src.utiilities.APImethods import APIMethodsImplementation
from ssqapitest.src.utiilities.baseTest import BaseTest
from ssqapitest.src.utiilities.payloads import APIPayloads

class CreateCustomer(object):



    def test_create_customer():
        """
          create payload : excel, json, DB reusble
          # send the payload to the endpoint : resuable
         # verify the response  response data can be use elsewhere
         # verify the status code
         verify data in the response
         verify data is created in the DB

        """
        data = APIPayloads('file')
        POST_method = APIMethodsImplementation()

        POST_method.post(endpoint=BaseTest.endpoints["CustomerEndpoint"],payloads=data,header=BaseTest.header,
                         auth=(BaseTest["access_key"],BaseTest["access_password"]))




