from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from userApp.models import *
from userApp.util import *
from coreApp.utils import *
from coreApp.config import *
import requests
import json

# title = {
#     'title': 'Index',
#     'header': 'BeeMindful-Buzz',
# }
# context = {
#     'title': title,
# }


theProj = PROJECT_ID
theKey = PRIVATE_KEY

def chatDash(request):
    title = {
        'title': 'Chat Dashboard',
        'header': 'Chat Dashboard - BeeMindful-Buzz'
    }
    user = User.objects.get(id=request.session['user_id'])
    # print(user)
    request.session['site'] = 'chat'
    site = request.session['site']
    request.session['role'] = user.role
    role = request.session['role']
    release = marquee()
    users = jsonUsersInChat()
    myChats = getMyChats(user.id)
    # print('mychats:', myChats, 'users:', users)
    if isinstance(myChats, list):
        request.session['chatStatus'] = "Good"
        chatStatus = request.session['chatStatus']
    if isinstance(myChats, dict):
        # customJson = {"user_role": user.role}
        send = sendUserToChat(user.username, user.email, user.firstName, user.lastName)
        request.session['chatStatus'] = "Good"
        print(send)
        chatStatus = request.session['chatStatus']
        # pass
    context = {
        'title': title,
        'role': role,
        'site': site,
        'user': user,
        'userVar': user.id,
        'release': release,
        'users': users,
        'myChats': myChats,
        'chatStatus': chatStatus,
    }
    return render(request, 'chatDash.html', context)

def authenticate(request, id):
    user = User.objects.filter(id=id)
    theSecret = 'BeeDevTechSquadServices'
    username = user.username
    secret = user.username+theSecret
    chatRole = user.role
    context = {
        'user': user,
        'username': username,
        'secret': secret,
    }
    # return render(request, 'newTemp.html', context)
    return JsonResponse(context, safe = False, content_type='application/json')

def multiChatFrame(request, id):
    title = {
        'title': 'Chat',
        'header': 'Chat - BeeMindful-Buzz'
    }
    user = User.objects.get(id=id)
    # print(user)
    request.session['site'] = 'chat'
    site = request.session['site']
    request.session['role'] = user.role
    role = request.session['role']
    release = marquee()
    context = {
        'title': title,
        'role': role,
        'site': site,
        'user': user,
        'release': release,
    }
    return render(request, 'chatFrameMulti.html', context)

def singleChatFrame(request, id):
    title = {
        'title': 'Chat',
        'header': 'Chat - BeeMindful-Buzz'
    }
    user = User.objects.get(id=id)
    # print(user)
    request.session['site'] = 'chat'
    site = request.session['site']
    request.session['role'] = user.role
    role = request.session['role']
    release = marquee()
    context = {
        'title': title,
        'role': role,
        'site': site,
        'user': user,
        'release': release,
    }
    return render(request, 'chatFrameSingle.html', context)