import requests
import json
import os
# URL = "http://127.0.0.1:8000/employeeData/"
# URL = "http://127.0.0.1:8000/ClassemployeeData/"
# URL = "http://127.0.0.1:8000/StudentAPI/"

# URL = "https://schoolcart.herokuapp.com/api/productimage/2/"
# files = open('/home/gautam/Django_Boys/DRF/DRF2/img/caf.png', 'rb')
# headers = {
#     'content-type': "multipart/form-data",
#     'accept': "application/json",
#     'apikey': "API0KEY0"
# }
# data = {
#     'id': 2,
#     'image': files
# }
# r = requests.patch(URL, data=data)
# print(r.json())


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    respnce = req.json()
    print(respnce)

# get_data()


def post_Data():
    data = {
        'name': 'Amit Singh',
        'roll': 3,
        'city': 'Alwar'
    }
    json_data = json.dumps(data)
    req = requests.post(url=URL, data=json_data)
    respnce = req.json()
    print(respnce)

# post_Data()


URL = "https://schoolcart.herokuapp.com/api/product/1/"


def update_data():
    data = {
        "id": 1,
        "sku": "vk",
    }
    # json_data = json.dumps(data)
    req = requests.patch(url=URL, data=data)
    respnce = req.json()
    print(respnce)

# update_data()


def delete_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    req = requests.delete(url=URL, data=json_data)
    respnce = req.json()
    print(respnce)

# delete_data(1)









URL = "https://schoolcart.herokuapp.com/api/productimage/2/"
files = open('/home/gautam/Django_Boys/DRF/DRF2/img/caf.png', 'rb')

with requests.patch(URL,files={'image':files}) as product_image_req:
    if product_image_req.status_code == 200:
        print("product_image: uploaded")
    else:
        print(product_image_req.status_code)
        print("product_image: some error")


data =  {
        'image': None,
        'product': product_req.json()['id'],
        }
img_file= {
            'image': files,
          }
with requests.post(URL,data=data,files=img_file) as product_image_req:
    if product_image_req.status_code == 201:
        print("product_image: uploaded")
    else:
        print(product_image_req.status_code)
        print("product_image: some error")