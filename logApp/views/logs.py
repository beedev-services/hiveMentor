from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *

# title = {
#     'title': 'Index',
#     'header': 'Hive Mentor',
# }
# context = {
#     'title': title,
# }
def logDash(request):
    title = {
        'title': 'Log Dashboard',
        'header': 'Hive Mentor - Log Dashboard',
    }
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view your logs')
        return redirect('/logReg/')
    user = User.objects.filter(id=request.session['user_id'])
    print('the user', user[0])
    request.session['site'] = 'logs'
    site = request.session['site']
    context = {
        'title': title,
        'user': user[0],
        'site': site
    }
    return render(request, 'logDash.html', context)

def newWeek(request):
    title = {
        'title':'Create Week',
        'header': 'Hive Mentor - Create Week'
    }
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view page')
        return redirect('/logReg/')
    user = User.objects.filter(id=request.session['user_id'])
    site = request.session['site']
    context = {
        'title': title,
        'user': user[0],
        'site': site
    }
    return render(request, 'createWeek.html', context)