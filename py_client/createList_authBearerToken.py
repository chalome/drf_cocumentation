import requests
from getpass import getpass


endpoint="http://localhost:8000/api/products/create_list/"
auth_endpoint="http://localhost:8000/api/auth/"

username=input("Enter username:\n")
password=getpass("what is your password:\n")

data={
    "title":"green pea",
    "content":"they are cereals sweet and natural and good for health",
    "price":600
}

auth_response=requests.post(auth_endpoint,json={"username":username,"password":password})
print(auth_response.json())

if auth_response.status_code==200:
    token=auth_response.json()['token']
    headers={
        "Authorization":f"Bearer {token}"
    }

    get_response=requests.post(endpoint,json=data,headers=headers)
    get_response=requests.get(endpoint,headers=headers)
    print(get_response.json())