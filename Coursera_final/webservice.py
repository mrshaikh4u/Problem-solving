import requests
import json
param = {
    "name" : "rahil",
    "first_name" : "shaikh"
}
print(param)
response = requests.post('https://www.google.com',json = param)
print(type(json.loads(response.request.body)))
# print(response.request.headers['Accept-Encoding'])
# response.raise_for_status()
# print(response.text[:300])
# print(response.status_code)