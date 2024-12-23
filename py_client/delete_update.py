import requests

# endpoint="http://localhost:8000/api/products/update/1/"
# data={
#     "title":"new beans",
#     "price":"900"
# }
# get_response=requests.put(endpoint,json=data)
# print(get_response.json())

product_id=input("What is the id of the product you want to delete?\n")
try:
    product_id=int(product_id)
except:
    print(f'{product_id} not a valid id!')
    product_id=None
    
if product_id:
    endpoint=f"http://localhost:8000/api/products/delete/{product_id}/"
    get_response=requests.delete(endpoint)
    print(get_response.status_code,get_response.status_code==204)