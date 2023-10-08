from django.conf import settings  # Import the settings module
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from logApp.models import *
from coreApp.utils import *
import os
import json


def userCount(request):
    users = list(User.objects.all().values())
    context = {
        'users': users
    }
    return JsonResponse(context, content_type="application.json")

def oneUser(request, user_id):
    users = list(User.objects.all().values())
    user = []
    for row in users:
        if row['id'] == user_id:
            user.append(row)
    # request.session['apiuser'] = user
    data = {
        'user': user
    }
    return JsonResponse(data, content_type="application.json")

def loggedUser(request, username):
    theUser = User.objects.get(username=username)
    user = theUser.username
    data = {
        'user': user
    }
    return JsonResponse(data, content_type="application.json")