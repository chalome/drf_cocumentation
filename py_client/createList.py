import requests

endpoint="http://localhost:8000/api/products/create_list/"
data={
    "title":"ripen mangoes",
    "content":"very ripen and natural",
    "price":250
}
# get_response=requests.post(endpoint,json=data)
get_response=requests.get(endpoint)
print(get_response.json())