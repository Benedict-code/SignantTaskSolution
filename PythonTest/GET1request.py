import requests
import json


base_url = "http://192.168.1.162:8080"

username = "usernamee"
password = "passwordd"

response = requests.get(base_url+"/api/auth/token", auth=(username, password))
print('the response for this GET request is')

print(response.status_code)
print(response.json())
print(response.headers.get("Content-Type"))

