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
    }
    return render(request, 'tempChat.html', context)

# def authenticate(request):
#     user = User.objects.get(id=request.session['user_id'])
#     print('theUser', user)
#     # print('from react', info)
#     res = requests.post(#'https://api.chatengine.io/users/',
#         data = {
#             'username': user.username,
#             'secret': user.username+'BeeDevServices'
#         },
#         headers = { theProj: theKey
#         }
#     )
#     print('data sent', res)
#     return res.json()
#     # return redirect('/chat/')

def authenticate(request):
    user =list( User.objects.filter(username=request.POST['username']))
    user = user[0]
    # print('theuser', user)
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
    print(user)
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