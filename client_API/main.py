import base64
import urllib.parse
import requests
import json
import timeit
import sys

####################################
image_path = "test.jpg"
image = open(image_path, 'rb')
image_read = image.read()
encoded = base64.encodestring(image_read)
image_encoded = encoded.decode('utf-8')
door_id = '5f8d390962ecf813570b518c'

####################################

verify_addr = 'http://192.168.0.105:3000/client/verify'
searchFace_addr = 'http://192.168.0.105:3000/client/searchFace'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Im5hbWUiOiJIb8OgbmcgxJDhu6ljIE1pbmgiLCJwZXJzb25hbElEIjoiMTg1MjEwOTcifSwiaWF0IjoxNjIxNTg1OTUyfQ.cQgPpZvuAMTXnJPKOq0OKymN5hHuMYFq0kNurqfLb50'

headers = {'Content-type': 'application/json'}
headers["Authorization"] = "Bearer "+ token
print('Connect to web: http://192.168.0.105:3000/client/verify \n')
response = requests.post(verify_addr, headers=headers)
print(response)
if (response.status_code == 200):
    print('Connect successfully!\n')
    print('Upload image to search...')
    data = {'door_id': door_id, 'image_encoded': image_encoded}
    data_json = json.dumps(data)
    response = requests.post(searchFace_addr, data = data_json, headers=headers)
    response = response.json()
    print(response)
