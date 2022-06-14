import requests



base_url = "http://192.168.1.162:8080"

header = {'Content-Type': 'application/json',
          'Token': 'MzE1NTc4ODM0NzE4MTI0OTQyNTIzNDI5MDYxODY1NDU5Njg4MjM1'}

response = requests.get(base_url+"/api/users", headers=header)
print('the response for this GET request is')

print(response.status_code)
print(response.json())
print(response.headers.get("Content-Type"))




#VALIDATION
assert response.status_code == 200


