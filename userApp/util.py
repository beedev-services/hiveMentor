import requests
from userApp.keys import *
from userApp.models import User
from coreApp.models import *
from django.utils import timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from django.conf import settings
from django.core.mail import send_mail

theKey = PRIVATE_KEY
theProj = PROJECT_ID
theUser = 'webmaster'
secret = CHAT_SECRET
weatherAPI = WEATHER_KEY

url = 'https://api.chatengine.io/users/'
adminUrl = "https://api.chatengine.io/users/me/"


def sendUserToChat(username, email, firstName, lastName, role):
    payload = {
        'username': username,
        'email': email,
        'first_name': firstName,
        'last_name': lastName,
        'secret': username+secret,
        'custom_json': {'role': role}
    }
    headers = {
        'PRIVATE-KEY': theKey
    }
    response = requests.post(url, json=payload, headers=headers)
    print('response sent in send user', response)
    return response

def sendCurrentUsersToChat():
    allUsers = User.objects.all()
    for user in allUsers:
        sendUserToChat(user.username, user.email, user.firstName, user.lastName, user.role)
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

def latLong(theZip):
    geoUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={theZip}{weatherAPI}"
    response = requests.get(geoUrl)
    res = response.json()
    return res

def getConditions(lat, lon):
    weatherUrl = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=imperial{weatherAPI}"
    response = requests.get(weatherUrl)
    res = response.json()
    return res


def sendSignupEmail(user):
    subject = 'Welcome to BeeMindful-Buzz'
    message = f'Hi {user.username}, thank you for registering for BeeMindful-Buzz. I am the owner and creator Melissa. This project has been a passion of mine for some time now I can not wait to get to know you! Please feel free to reach out if you have any questions'
    email_from = settings.EMAIL_HOST_ALT_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )
    
