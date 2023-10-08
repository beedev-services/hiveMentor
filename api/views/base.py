from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from coreApp.utils import *
from userApp.models import *
import os
import json


status = {
    "API Status": "Running"
}

def apiBase(request):
    return JsonResponse(status, content_type="application.json")

def releaseDates(request):
    marqueeData = marquee()
    return JsonResponse(marqueeData, content_type="application.json")

def board(request):
    status = projBoard()
    data = {
        'status': status
    }
    return JsonResponse(data, content_type="application.json")

def apiLogin(request):
    pass

@login_required
def testApi(request):
    status = 'API running'
    user = User.objects.get(id=request.session['user_id'])
    print(user)
    data = {
        'status': status,
        'user': user,
    }
    return JsonResponse(data, content_type="application.json")