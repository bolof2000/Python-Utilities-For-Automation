import json
class APIPayloads(object):
    """
    payloads can be in form of :
    excel file
    json file
    this class returns payload for different API endpoints
    """

    def __init__(self,file):
        with open(file,'r') as data:
            self.data = json.load(data)

    def customer_payloads(self):
        return self.data


    def price_payloads(self):
        return self.data

    def products_payloads(self,data):
        return self.data

test = APIPayloads('cusomerAPI.json')
print(test.customer_payloads())
