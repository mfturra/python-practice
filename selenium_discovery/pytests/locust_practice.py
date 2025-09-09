import requests
import json
from fastapi import ( FastAPI, Request )
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from locust import HttpUser, task, between

fake_db = {
    "userone": {
        "username": "userone",
        "full_name": "userone",
        "password": "fakesecret1"
    },
    "usertwo": {
        "username": "usertwo",
        "password": "fakesecret2"
    }
}

# creation of app work
app = FastAPI()


# def hash_password(password: str):
#     return "fake_hash" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str

# Submit post request to okta sign in and acquire output
okta_login = "https://login.okta.com"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(okta_login, auth=(user,pwd), headers=headers)
response.raise_for_status()

print(response.status_code)

# Check for HTTP codes other than 200
if response.status_code == 201: 
    print('Status:', response.status_code)
    print('Response:',response.json())
    data=response.json()
    print(data['result']['StatusDescription'])
    print(data['result']['IncidentNumber'])
    print(data['result']['Link'])
    exit()


# @app.get("/")
# async def home(request: Request): 
#     logging.info(f"Request sent to: {str(request.url)}")


# # payload build
# url = 'http://dev-aizone.mgb.org'






# # host_url = "https://regres.in"

# class UserRequest(HttpUser):
#     weight = 2
#     host = "https://regres.in"
#     headers = {
#         "x-api-key": "reqres-free-v1"  # Replace with your actual API key
#     }

#     # Optional: Define a wait time between requests
#     wait_time = between(1, 3)  # Random wait time between 1 to 3 seconds

#     @task
#     def get_users(self):
#         response = self.client.get("/api/users", headers=self.headers)

#         if response.status_code == 200:
#             print("Request successful!")
#             print(response.json())
#         else:
#             print(f"Request failed with status code: {response.status_code}")
#             print(response.text)

# class UserRequest(HttpUser):
#     weight = 2

#     host = "https://regres.in"
#     api_key = "reqres-free-v1"
#     headers = {
#         "x-api-key": api_key
#     }
#     wait_time = between(1,3)

#     @task
#     def get_users(self):
#         response = self.client.get("/api/users?page=2", headers=self.headers)

#         if response.status_code == 200:
#             print("Request successful!")
#             print(response.json())
#         else:
#             print(f"Request failed with status code: {response.status_code}")
#             print(response.text)

#     # @task
#     # def search(self):
#     #     self.client.post("/api/users")