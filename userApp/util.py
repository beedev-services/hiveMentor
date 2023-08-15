import requests
from userApp.keys import *
from userApp.models import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

theKey = PRIVATE_KEY
theProj = PROJECT_ID
theUser = 'webmaster'
secret = 'BeeDevServices'
# weatherAPI = '&appid=e2dce74ca5407e4678b17b94a72fe7df'
weatherAPI = '&appid=179fcd38509ce9a4671ca1be23eac6ba'

url = 'https://api.chatengine.io/users/'
adminUrl = "https://api.chatengine.io/users/me/"


def sendUserToChat(username, email, firstName, lastName, role):
    payload = {
        'username': username,
        'email': email,
        'first_name': firstName,
        'last_name': lastName,
        'secret': username+'BeeDevServices',
        'custom_json': {'role': role}
    }
    headers = {
        'PRIVATE-KEY': theKey
    }
    response = requests.post(url, json=payload, headers=headers)

def sendCurrentUsersToChat():
    allUsers = User.objects.all()
    for user in allUsers:
        sendUserToChat(user.username, user.email, user.firstName, user.lastName, user.role)

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

def latLong(theZip):
    geoUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={theZip}{weatherAPI}"
    response = requests.get(geoUrl)
    res = response.json()
    return res