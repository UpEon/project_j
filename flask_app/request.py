import requests
url = 'http://localhost:5000/api'
r = requests.post(url, json={'exp':1.8,})
print(r.json())


import requests
import json
import csv
import pandas as pd

url = 'http://0.0.0.0:5000/api/'

data = pd.read_csv('C:\\Users\\JEON_SANGEON\\codestates\\Section3\\Project\\flask_app\\data\\kc_house_data.csv')
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)