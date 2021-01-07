import requests
import json

# URL = "http://127.0.0.1:8000/employeeData/"
# URL = "http://127.0.0.1:8000/ClassemployeeData/"
URL = "http://127.0.0.1:8000/StudentAPI/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.get(url=URL,data=json_data)
    respnce = req.json()
    print(respnce)
    
# get_data(1)


def post_Data():
    data = {
        'name':'Amit Singh',
        'roll':3,
        'city':'Alwar'
    }
    json_data = json.dumps(data)
    req = requests.post(url=URL,data=json_data)
    respnce = req.json()
    print(respnce)

# post_Data()


def update_data():
    data = {
        'id':3,
        'name':'Amit Kumar',
        # 'salery':25000,
    }
    json_data = json.dumps(data)
    req = requests.put(url=URL,data=json_data)
    respnce = req.json()
    print(respnce)

# update_data()


def delete_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.delete(url=URL,data=json_data)
    respnce = req.json()
    print(respnce)

delete_data(1)