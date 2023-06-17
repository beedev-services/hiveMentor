from django.shortcuts import render, redirect
from django.contrib import messages

# title = {
#     'title': 'Index',
#     'header': 'Hive Mentor',
# }
# context = {
#     'title': title,
# }
def index(request):
    title = {
        'title': 'Log Dashboard',
        'header': 'Hive Mentor - Log Dasbboards',
    }
    context = {
        'title': title,
    }
    return render(request, 'logTemp.html', context)