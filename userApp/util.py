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


