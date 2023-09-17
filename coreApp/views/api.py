from django.conf import settings  # Import the settings module
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from logApp.models import *
from logApp.views.logs import categories
from userApp.util import *
from coreApp.apiUtil import *
from coreApp.adminUtil import *
import os
import json

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

def filter_logs(log_data, log_level):
    # Define a list of keywords that indicate database-related log messages
    database_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'COMMIT', 'ROLLBACK', 'ALTER', 'CREATE', 'DROP']

    # Filter log entries based on log level and exclude database-related messages
    filtered_logs = [entry for entry in log_data if entry['level'] == log_level and not any(keyword in entry['message'] for keyword in database_keywords)]

    return filtered_logs


def getLogs(request):
    log_file_path = os.path.join(settings.BASE_DIR, 'json', 'logfile.json')  # Correct relative path
    try:
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            log_data = json.load(log_file)
            log_level_to_filter = 'INFO'
            filtered_logs = filter_logs(log_data, log_level_to_filter)
        return JsonResponse({'logs': filtered_logs})
    except FileNotFoundError:
        return JsonResponse({'error': 'Log file not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data in log file'}, status=500)


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