import requests

endpoint="http://localhost:8000/api/products/create/"
data={
    "title":"la porte magique",
    "price":"100"
}
get_response=requests.post(endpoint,json=data)
print(get_response.json())