import requests
from userApp.keys import *
from userApp.models import User
from coreApp.models import *
from django.utils import timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from django.conf import settings
from django.core.mail import send_mail
import json

import logging

logger = logging.getLogger(__name__)
# def my_view(request):
#     # ...
#     logger.debug('This is a debug message')
#     logger.info('This is an info message')
#     logger.warning('This is a warning message')
#     logger.error('This is an error message')
#     logger.critical('This is a critical message')
#     # ...


theKey = PRIVATE_KEY
theProj = PROJECT_ID
theUser = 'webmaster'
secret = CHAT_SECRET
weatherAPI = WEATHER_KEY

url = 'https://api.chatengine.io/users/'
adminUrl = "https://api.chatengine.io/users/me/"


def sendUserToChat(username, email, firstName, lastName):
    payload = {
        'username': username,
        'secret': username+secret,
        'email': email,
        'first_name': firstName,
        'last_name': lastName
    }
    headers = {
        'PRIVATE-KEY': theKey
    }
    print(payload, headers, url)
    logger.info(payload, headers, url)

    try:
        response = requests.post(url, json=payload, headers=headers)
        responseData = response.json() if response.status_code == 200 else None
        print('Response:', response.status_code, responseData)
        logger.info('Response:', response.status_code, responseData)
        return response
    except Exception as e:
        print('Error:', str(e))
        logger.error('Error:', str(e))
        return None

def sendCurrentUsersToChat():
    allUsers = User.objects.all()
    for user in allUsers:
        sendUserToChat(user.username, user.email, user.firstName, user.lastName)
    print('loop done in send current')

def getUsersInChat():
    payload={}
    headers = {
        'PRIVATE-KEY': PRIVATE_KEY
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
    payload = ""
    # "{\n    \"username\": \"adam_la_morre\",\n    \"email\": \"adam_la_morre@chatengine.io\",\n    \"first_name\": \"Adam\",\n    \"last_name\": \"La Morre\",\n    \"custom_json\": {\n        \"custom_json\": 2001\n    }\n}"
    headers = {
    'Project-ID': theProj,
    'User-Name': theUser,
    'User-Secret': theUser+secret
    }

    response = requests.request("PATCH", adminUrl, headers=headers, data=payload)

    print(response.text)


