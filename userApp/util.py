import requests
from userApp.keys import *
from userApp.models import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

theKey = PRIVATE_KEY
theProj = PROJECT_ID
theUser = 'webmaster'
secret = 'BeeDevServices'

url = 'https://api.chatengine.io/users/'
adminUrl = "https://api.chatengine.io/users/me/"

def sendUserToChat(username, email, firstName, lastName):
    payload = {
        'username': username,
        'email': email,
        'first_name': firstName,
        'last_name': lastName,
        'secret': username+'BeeDevServices'
    }
    headers = {
        'PRIVATE-KEY': theKey
    }
    response = requests.post(url, json=payload, headers=headers)

def sendCurrentUsersToChat():
    allUsers = User.objects.all()
    for user in allUsers:
        sendUserToChat(user.username, user.email, user.firstName, user.lastName)

def getUsersInChat():
    payload={}
    headers = {
        'PRIVATE-KEY': 'd7e2e051-741c-4ed0-933b-9bf26f6029c2'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def getAdminAcct():
    payload={}
    headers = {
    'Project-ID': theProj,
    'User-Name': theUser,
    'User-Secret': theUser+secret
    }
    response = requests.request("GET", adminUrl, headers=headers, data=payload)
    print(response.text)

def updateUserAcct():
    payload = "{\n    \"username\": \"adam_la_morre\",\n    \"email\": \"adam_la_morre@chatengine.io\",\n    \"first_name\": \"Adam\",\n    \"last_name\": \"La Morre\",\n    \"custom_json\": {\n        \"custom_json\": 2001\n    }\n}"
    headers = {
    'Project-ID': theProj,
    'User-Name': theUser,
    'User-Secret': theUser+secret
    }

    response = requests.request("PATCH", adminUrl, headers=headers, data=payload)

    print(response.text)
