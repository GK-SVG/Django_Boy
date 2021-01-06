import requests
import json

URL = "http://127.0.0.1:8000/employeeData/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.get(url=URL,data=json_data)
    respnce = req.json()
    print(respnce)
    
# get_data()


def post_Data():
    data = {
        'name':'Gaurav',
        'salery':15000,
        'city':'Alwar'
    }
    json_data = json.dumps(data)
    req = requests.post(url=URL,data=json_data)
    respnce = req.json()
    print(respnce)

post_Data()