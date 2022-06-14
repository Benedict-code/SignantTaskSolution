import requests

base_url = "http://192.168.1.162:8080"

body = {
    "username":"usernamee",
    "password":"passwordd",
    "firstname":"firstnamee",
    "lastname":"lastnamee",
    "mobile":"+358400000000",
    "address":"finland"
}
header = {"Content-Type":"application/json",
          "Token": "MzE1NTc4ODM0NzE4MTI0OTQyNTIzNDI5MDYxODY1NDU5Njg4MjM1"}

response = requests.put(base_url+"/api/users/{username}", data=body, headers=header)
print('the response for this PUT request is')

print(response.status_code)
print(response.json())
print(response.headers.get("Content-Type"))

#The status code is 400>. It was not able to add a new user and hence, status code 201 was not optainable.

#VALIDATION