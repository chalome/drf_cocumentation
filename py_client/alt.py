import requests

endpoint="http://localhost:8000/api/products/create_list_/"
data={
    "title":"the curtain",
    "price":"459"
}
get_response=requests.get(endpoint,json=data)
print(get_response.json())