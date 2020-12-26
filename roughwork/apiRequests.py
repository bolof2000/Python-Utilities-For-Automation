import json
import requests
endPoints = {'getBook':'http://216.10.245.166/Library/GetBook.php','addBook':'http://216.10.245.166/Library/Addbook.php'}
addbookdata = {
    "name": "Learn Appium Automation with Pythpn",
    "isbn": "bdcddd",
    "aisle": "22fd922",
    "author":"Dammy Bolofinde"
}
headers = {'Content-Type':'application/json'}

def create_data_API():
    addBook_response = requests.post(url=endPoints['addBook'],json=addbookdata,)
    return addBook_response.json()

def getBookByAuthor():
   # url = 'http://216.10.245.166/Library/GetBook.php'
    payload = {'AuthorName':'Rahul Shetty2'}
    response = requests.get(url=endPoints['getBook'],params=payload,)
    response_json= response.json()
    for author in response_json:
        return author['']
    return response_json

def deleteBookAPITest():
    delete_book_response = requests.delete()


print(getBookByAuthor())
print(create_data_API())



