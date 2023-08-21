from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from logApp.models import *
from logApp.views.logs import categories
from userApp.util import *
from coreApp.apiUtil import *

status = {
    "API Status": "Running"
}

def apiBase(request):
    return JsonResponse(status, content_type="application.json")

def userCount(request):
    users = list(User.objects.all().values())
    context = {
        'users': users
    }
    return JsonResponse(context, content_type="application.json")

def allFoodData(request):
    fList = list(FoodList.objects.all().values())
    context = {
        'fList': fList,
    }
    return JsonResponse(context, content_type="application.json")

def foodData(request, cat):
    fList = list(FoodList.objects.filter(category=cat).values())
    context = {
        'fList': fList,
    }
    return JsonResponse(context, content_type="application.json")

def releaseDates(request):
    marqueeData = marquee()
    return JsonResponse(marqueeData, content_type="application.json")

def board(request):
    status = projBoard()
    data = {
        'status': status
    }
    return JsonResponse(data, content_type="application.json")