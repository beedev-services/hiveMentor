from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from userApp.models import *
# from userApp.util import authenticate
from userApp.keys import *
import requests

# title = {
#     'title': 'Index',
#     'header': 'Hive Mentor',
# }
# context = {
#     'title': title,
# }
theProj = PROJECT_ID
theKey = PRIVATE_KEY

def chatDash(request):
    title = {
        'title': 'Chat Dashboard',
        'header': 'Chat Dashboard - Hive Mentor'
    }
    user = User.objects.get(id=request.session['user_id'])
    # print(user)
    request.session['site'] = 'chat'
    site = request.session['site']
    request.session['role'] = user.role
    role = request.session['role']
    context = {
        'title': title,
        'role': role,
        'site': site,
        'user': user,
        'userVar': user.id,
    }
    return render(request, 'chatDash.html', context)

def authenticate(request, id):
    user = User.objects.filter(id=id)
    theSecret = 'BeeDevServices'
    username = user.username
    secret = user.username+theSecret
    context = {
        'user': user,
        'username': username,
        'secret': secret,
    }
    # return render(request, 'newTemp.html', context)
    return JsonResponse(context, safe = False, content_type='application/json')

def chatFrame(request, id):
    title = {
        'title': 'Chat',
        'header': 'Chat - Hive Mentor'
    }
    user = User.objects.get(id=id)
    # print(user)
    request.session['site'] = 'chat'
    site = request.session['site']
    request.session['role'] = user.role
    role = request.session['role']
    context = {
        'title': title,
        'role': role,
        'site': site,
        'user': user
    }
    return render(request, 'chatFrame.html', context)