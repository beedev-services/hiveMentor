from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
import bcrypt


def index(request):
    title = {
        'title': 'Index - Hive Mentor',
        'header': 'Hive Mentor',
    }
    context = {
        'title': title,
    }
    return render(request, 'temp.html', context)
