import requests
from coreApp.config.keys import *
from userApp.models import User
from coreApp.models import *
import json


theKey = PRIVATE_KEY
theProj = PROJECT_ID
theUser = 'webmaster'
secret = CHAT_SECRET
weatherAPI = WEATHER_KEY

user_url = 'https://api.chatengine.io/users/'
adminUrl = "https://api.chatengine.io/users/me/"
chat_url = 'https://api.chatengine.io/chats/'


def sendUserToChat(username, email, firstName, lastName):
    payload = {
        'username': username,
        'secret': username+secret,
        'email': email,
        'first_name': firstName,
        'last_name': lastName,
        'custom_json': "{'user_role': 'General'}",
    }
    headers = {
        'PRIVATE-KEY': theKey
    }
    print(payload, headers, user_url)
    try:
        response = requests.post(user_url, json=payload, headers=headers)
        responseData = response.json() if response.status_code == 200 else None
        print('Response:', response.status_code, responseData)
        return response
    except Exception as e:
        print('Error:', str(e))
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
    response = requests.request("GET", user_url, headers=headers, data=payload)
    print('response in call',response)
    return response.text

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
    headers = {
    'Project-ID': theProj,
    'User-Name': theUser,
    'User-Secret': theUser+secret
    }
    response = requests.request("PATCH", adminUrl, headers=headers, data=payload)
    print(response.text)

def sendUserToGroup(username, chatID, chatAdmin):
    addUserChat_urlFull = chat_url+chatID+"/people/"
    payload = { 'username': username }
    headers = {
        'Project-ID': theProj,
        'User-Name': chatAdmin,
        'User-Secret': chatAdmin+secret
    }
    print(payload, headers, addUserChat_urlFull)
    try:
        response = requests.post(addUserChat_urlFull, json=payload, headers=headers)
        responseData = response.json() if response.status_code == 200 else None
        print('Response:', response.status_code, responseData)
        return response
    except Exception as e:
        print('Error:', str(e))
        return None

def sendCurrentUsersToGroup(chatID, chatAdmin):
    allUsers = User.objects.all()
    for user in allUsers:
        sendUserToGroup(user.username, chatID, chatAdmin)
    print('loop done in send current to group')

def getCurrentUsersInGroup(chatID, chatAdmin):
    fullUrl = chat_url+chatID+"/people/"
    payload={}
    headers = {
        'Project-ID': theProj,
        'User-Name': chatAdmin,
        'User-Secret': chatAdmin+secret
    }
    print(payload, headers, fullUrl)
    try:
        response = requests.get(fullUrl, json=payload, headers=headers)
        responseData = response.json() if response.status_code == 200 else None
        print('Response:', response.status_code, responseData)
        return response
    except Exception as e:
        print('Error:', str(e))
        return None

def getMyChats(userId):
    user = User.objects.get(id=userId)
    payload={}
    headers={
        'Project-ID': theProj,
        'User-Name': user.username,
        'User-Secret': user.username+secret
    }
    print(chat_url, headers)
    response = requests.request("GET", chat_url, headers=headers, data=payload)
    print("res.text:",response.text)
    chats = json.loads(response.text)
    return chats

def jsonUsersInChat():
    theUsers = getUsersInChat()
    users = json.loads(theUsers)

    for user in users:
        temp = json.loads(user['custom_json'].replace("'", "\""))
        user['custom_json'] = temp

    return users