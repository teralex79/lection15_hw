#!/bin/python3.6

import requests
import json

r_con = requests.get('http://192.168.56.103:2376/containers/json?all=1')
r_con_json = json.loads(r_con.text)
r_img = requests.get('http://192.168.56.103:2376/images/json?all=1')
r_img_json = json.loads(r_img.text)

print(r_con_json[0].keys())
print(r_con_json[0]['Names'])
