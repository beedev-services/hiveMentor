import requests
from userApp.keys import *
from userApp.models import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

theKey = PRIVATE_KEY
theProj = PROJECT_ID

def sendUserToChat(username, email, firstName, lastName):

    url = 'https://api.chatengine.io/users/'

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
    if response.status_code == 200:
        print('User information sent successfully')
    else:
        print('Failed to send user information')

def sendCurrentUsersToChat():
    allUsers = User.objects.all()
    # print(allUsers)
    sentUser = []
    failedUser = []
    for user in allUsers:
        # print('theUser', user)
        # print('theUser.id', user.id)
        sendUserToChat(user.username, user.email, user.firstName, user.lastName)

# async def authenticate(user):
#     res = requests.put('https://api.chatengine.io/users/',
#         data = {
#             'username': user.username,
#             'secret': user.username+'BeeDevServices'
#         },
#         headers = { theProj: theKey
#         }
#     )
#     return res.json()