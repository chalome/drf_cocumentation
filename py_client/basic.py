import requests

# endpoint="http://httpbin.org/"
# endpoint="http://httpbin.org/anything"
# endpoint="http://httpbin.org/"
endpoint="http://localhost:8000/api/"
# get_response=requests.get(endpoint)#http request
# print(get_response.text)#print raw text response
# print(get_response.json()['message'])#python dictionary
# print(get_response.json())#python dictionary
# print(f'The status code is: {get_response.status_code}')

# HTTP requests -> HTML
# REST API HTTP Request -> JSON


get_response=requests.post(endpoint,json={"title":"legumes vertes","content":"beautiful and delicious","price":500})
print(get_response.json())