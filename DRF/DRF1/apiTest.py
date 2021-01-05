import requests
import json

URL = "http://127.0.0.1:8000/stuCreate/"

data = {
    'name':"Ashu",
    'roll':4,
    'cit':8,
    'test':9
}
data = json.dumps(data)
resp = requests.post(url=URL,data=data)
print(resp.json())