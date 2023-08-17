from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from logApp.models import *
from logApp.views.logs import categories

status = {
    "API Status": "Running"
}

def apiBase(request):
    return JsonResponse(status, content_type="application.json")

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