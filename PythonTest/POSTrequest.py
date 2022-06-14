import json

import requests

#REGISTER NEW USER

base_url = "http://192.168.1.162:8080"

body = {
    "username":"usernamee",
    "password":"passwordd",
    "firstname":"firstnamee",
    "lastname":"lastnamee",
    "mobile":"+358400000000"
}
header = {"Content-Type":"application/json"}

response = requests.post(base_url+"/api/users", data=body, headers=header)
print('the response for this POST request is')

print(response.status_code)
print(response.json())
print(response.headers.get("Content-Type"))


#The status code is 400. It was not able to add a new user and hence, status code 201 was not optainable.


#VALIDATIONS



