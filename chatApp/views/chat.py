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
    print(user)
    request.session['site'] = 'chat'
    site = request.session['site']
    request.session['role'] = user.role
    role = request.session['role']
    context = {
        'title': title,
        'role': role,
        'site': site,
    }
    return render(request, 'tempChat.html', context)

def authenticate(request):
    user = User.objects.get(id=request.session['user_id'])
    print('theUser', user)
    res = requests.put('https://api.chatengine.io/users/',
        data = {
            'username': user.username,
            'secret': user.username+'BeeDevServices'
        },
        headers = { theProj: theKey
        }
    )
    return res.json()
    # return redirect('/chat/')